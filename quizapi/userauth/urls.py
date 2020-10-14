from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('signup/',views.CreateUserAccount.as_view()),
]
