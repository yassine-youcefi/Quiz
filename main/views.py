from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Quiz, Question, Answer, Result
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
from .forms import QuizForm, QuizEditForm

# from rest_framework.views import APIView


def index(request):
    return render(request, 'templates/index.html')
class QuizzesList(ListView):
    model = Quiz
    template_name = 'templates/quizes.html'

def quiz_detail(request, pk):
    context = {
        'quiz': Quiz.objects.get(pk=pk)
    }
    return render(request, 'templates/quize_details.html', context)        

def quiz_data(request, pk):
    quiz = Quiz.objects.get(pk=pk)
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
            question = Question.objects.get(text=key)
            questions.append(question)

        user = request.user
        print("user = ",user)
        quiz = Quiz.objects.get(pk=pk)
        multiple_answers = 100 / len(questions)

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

# for admin only
def quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print("form not valid")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    if request.method == 'GET':
        form = QuizForm()
    return render(request, 'templates/quiz_create.html', {'form': form})

# for admin only
def quiz_update(request, pk):
    if request.method == 'POST':
        form = QuizEditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
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
