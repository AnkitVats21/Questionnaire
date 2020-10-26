from rest_framework import serializers
from .models import Quiz, Question, Answers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Quiz
        fields  = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Question
        fields  = '__all__'

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Answers
        fields  = '__all__'