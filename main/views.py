from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Quiz, Question, Answer, Result
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
from .forms import QuizForm, QuizEditForm,QuestionForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .decorators import allowed_users


# from rest_framework.views import APIView


def index(request):
    user_group = []
    for group in request.user.groups.all():
        user_group.append(group.name)

    context = {
        "user_group" : user_group,
    }    
    return render(request, 'templates/index.html', context=context)

# __________/ for students \____________
class QuizzesList(ListView):
    model = Quiz
    template_name = 'templates/quizzes.html'

# __________/ for admin \____________
class QuizzesListAdmin(ListView):
    model = Quiz
    template_name = 'templates/admin_quizzes.html'    



def quiz_detail(request, pk):
    questions_length = get_object_or_404(Quiz, pk=pk).get_questions().count()
    print("questions_length = ",questions_length)
    context = {
        'questions_length' : questions_length,
        'quiz': get_object_or_404(Quiz, pk=pk)
    }
    return render(request, 'templates/quize_details.html', context)        

def quiz_data(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = []
    for question in quiz.get_questions():
        # questions.append(qu estion.text)
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)

        questions.append({str(question):answers})
    
    return JsonResponse({
        'questions': questions,
        'time' : quiz.time,
        })

def quiz_result(request, pk):
    # check if the request is ajax 
    if request.is_ajax():
        print(request.POST)
        questions = []
        results = []
        correct_answers = None
        score = 0
        
        # get pos data from ajax request
        data = request.POST
        data = data.dict()
        data.pop('csrfmiddlewaretoken')
        
        # append all post data questions to the questions list
        for key in data.keys():
            get_object_or_404(Quiz, pk=pk)
            question = get_object_or_404(Question, text=key)
            questions.append(question)

        user = request.user
        print("user = ",user)
        quiz = Quiz.objects.get(pk=pk)
        try:
            multiple_answers = 100 / len(questions)
        except ZeroDivisionError:
            multiple_answers = 0
        # loop over questions 
        for question in questions:
            # get the selected answer
            selected_answer = request.POST.get(question.text)
            # check if the answer is not empty 
            if selected_answer != "" :
                # get the question of the selected answer
                questins_of_answer = Answer.objects.filter(question=question)
                # loop over the answers of the question
                for answer in questins_of_answer:
                    # check if the selected answer is the same as the answer
                    if selected_answer == answer.text:
                        # check if the answer is correct
                        if answer.correct:
                            score += 1 
                            correct_answers = answer.text
                    else:
                        if answer.correct:
                            correct_answers = answer.text  
                # append the result to the results list if the answer is correct and not none
                results.append({question.text : {'correct_answer': correct_answers, 'answered': selected_answer}})                  
            else:
                # get the correct answer of the question
                questins_of_answer = Answer.objects.filter(question=question) 
                for answer in questins_of_answer:
                    if answer.correct:
                        correct_answer = answer.text 
                results.append({question.text :  {'correct_answer': correct_answer, 'answered': 'awnser not found'}}) 

        # calculate the score 
        _score = score * multiple_answers
        # save the result to the database
        Result.objects.create(user=user, quiz=quiz, score=_score)

        
        if _score >= quiz.required_score:
            return JsonResponse({'passed': True, 'score': _score, 'results': results})
        else:
            return JsonResponse({'passed': False,'score': _score, 'results': results})   

def quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Quiz is create successfuly for ')
            return redirect('main:quiz_list_admin')
        else:
            print("form not valid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    if request.method == 'GET':
        form = QuizForm()
    return render(request, 'templates/quiz_create.html', {'form': form})

def quiz_update(request, pk):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=pk)
        print("quiz = ",str(quiz))

        form = QuizEditForm(request.POST, instance=quiz)
        if form.is_valid():
            obj = form.save(commit= False)
            obj.save()
            messages.success(
            request, f'Quiz is updated successfuly for {quiz.name}')
            context= {'form': form}

            return redirect('main:quiz_list_admin')
        else:
            print("form not valid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        quiz = Quiz.objects.get(pk=pk)
        form = QuizEditForm(instance=quiz) 

        context = {
            'quiz': quiz,
            'form': form
        }
        return render(request, 'templates/quiz_update.html', context)

def quize_delete(request,pk):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=pk)
        quiz.delete()
        messages.success(
            request, f'Quiz is deleted successfuly for {quiz.name}')
        return redirect('main:quiz_list_admin')
    else:
        quiz = Quiz.objects.get(pk=pk)
        context = {'quiz' : quiz}
        return render(request, 'templates/quiz_delete.html', context)


def question_create(request, pk):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print("pk = ",pk)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Question is create successfuly for ')
            return redirect('main:quiz_detail', pk=pk)
        else:
            print("form not valid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    if request.method == 'GET':
        quiz = get_object_or_404(Quiz, pk=pk)
        form = QuestionForm()
        context = {'form': form
                ,'quiz': quiz}
    return render(request, 'templates/question_create.html',context=context )
