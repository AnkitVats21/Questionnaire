from .models import Question, Answers, Quiz
from .permissions import IsTeacher
from rest_framework import viewsets, status, generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import QuizSerializer, QuestionSerializer, AnswersSerializer
import random
import string
class QuizListView(APIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsTeacher]
    serializer_class  = QuizSerializer
    queryset            = Quiz.objects.all()

    def get_random_string(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(9))

    def get(self, request):
        quiz        = Quiz.objects.all()
        serializer  = QuizSerializer(quiz, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request = request.data.copy()
        print(request)
        q_code  = self.get_random_string()
        obj = Quiz.objects.filter(quiz_code=q_code)
        while len(obj)!=0:
            q_code  = self.get_random_string()
            obj = Quiz.objects.filter(quiz_code=q_code)
        request['quiz_code'] = q_code
        serializer  = QuizSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizView(APIView):
    def patch(self, request):
        serializer  = QuizSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionListView(APIView):
    def get(self, request):
        question    = Question.objects.all()
        serializer  = QuestionSerializer(question, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionView(APIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsTeacher]
    serializer_class  = QuestionSerializer
    queryset          = Question.objects.all()

    def get(self, request, pk):
        quiz        = Question.objects.filter(id=pk)
        serializer  = QuestionSerializer(quiz, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        user    = request.user
        if user.teacher:
            serializer  = QuestionSerializer(data=request)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data":"user is not a teacher."}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user    = request.user
        if user.teacher:
            obj = Question.objects.filter(pk=pk)
            serializer  = QuestionSerializer(request.user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data":"user is not a teacher."}, status=status.HTTP_400_BAD_REQUEST)

class AnswersView(APIView):
    def get(self, request, pk):
        user    = request.user
        ans     = Answers.objects.filter(user=user).filter(quiz=pk)
        serializer= AnswersSerializer(ans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = AnswersSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
