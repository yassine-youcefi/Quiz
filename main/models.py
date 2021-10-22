from django.db import models
from connect.models import User
# from django.contrib.auth.models import User

QUESTION_TYPE = (
        ('MCQ', 'Multiple Choice'),
        ('TF', 'True or False'),
        ('FIB', 'Fill in the Blank'),)
        

class Quiz(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField(default=0)
    time = models.IntegerField(help_text="Time in minutes", default=0)
    # difficluty = models.CharField(max_length=10)
    required_score = models.IntegerField(help_text="Score required to pass the quiz")

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question.all()[:self.number_of_questions]

class Question(models.Model):
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="question")
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer.all()

class Answer(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usrt_answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    cereated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="result")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

