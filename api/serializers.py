from rest_framework import serializers
from connect.models import *
from main.models import *



# _______________ / User serializers \_______________


class GetUserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    
    def get_groups(self, obj):
        my_groups = []

        for group in obj.groups.all():
            group_dict =  {
                'id': group.id,
                'name': group.name,
            }
            my_groups.append(group_dict)


        return my_groups
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')    

class PutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

# _______________ / Quiz serializers \_______________
class GetQuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'topic', 'number_of_questions', 'time', 'required_score')

class GetQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id','admin', 'name', 'topic', 'number_of_questions', 'time', 'required_score')



# _______________ / Questions serializers \_______________

class GetAnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('user', "question", "text")

class GetQuestionListSerializer(serializers.ModelSerializer):
    answer = GetAnswersSerializers(many=True)
    class Meta:
        model = Question
        fields = ('id', 'question_type', 'quiz', 'text', "answer")

class GetQuestionSerializer(serializers.ModelSerializer):
    answer = GetAnswersSerializers(many=True)
    class Meta:
        model = Question
        fields = ('id', 'question_type', 'quiz', 'text','answer')

class PostQuestionSerializer(serializers.ModelSerializer):
    answer = GetAnswersSerializers(many=True,read_only=True)

    class Meta:
        model = Question
        fields = ('question_type', 'quiz', 'text', 'answer')

class PutQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_type', 'quiz', 'text', 'answer')