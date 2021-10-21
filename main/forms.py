from django.forms import ModelForm
from .models import Quiz, Question, Answer



# create form for Quiz model (create quiz) 
class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'topic', 'number_of_questions', 'time', 'required_score']

# cerate form for Quiz model (edit quiz)
class QuizEditForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'topic', 'number_of_questions', 'time', 'required_score']

# # create form for Question model (create question)
# class QuestionForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = '__all__'

# # create form for Answer model (create answer)
# class AnswerForm(ModelForm):
#     class Meta:
#         model = Answer
#         fields = '__all__'
