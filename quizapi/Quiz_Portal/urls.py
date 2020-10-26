from django.urls import path
from django.conf.urls import url, include
from Quiz_Portal import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'api/quizes', views.QuizView, basename='quiz')

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('api/quizes/', views.QuizListView.as_view()),
    path('api/quiz/<pk>/', views.QuestionView.as_view()),
    path('api/questions/', views.QuestionListView.as_view()),
    path('api/answer/<pk>/', views.AnswersView.as_view()),
]
