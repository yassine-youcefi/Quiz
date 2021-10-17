from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField(default=0)
    time = models.IntegerField(help_text="Time in minutes", default=0)
    required_score = models.IntegerField(help_text="Score required to pass the quiz")

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # answer = models.CharField(max_length=200)
    # points = models.IntegerField(default=0)


    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    cereated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
