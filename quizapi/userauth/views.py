from validate_email import validate_email
from .models import User
from rest_framework import viewsets, status, generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import Http404
from django.template.loader import render_to_string
from django.shortcuts import render
from .serializers import UserSerializer
import re 
  
regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

def check(email):  
    if(re.search(regex,email)):  
        return True   
    else:  
        return False


class CreateUserAccount(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        user_email  = request.data.get("email")
        req_data    =request.data
        if check(user_email):
            user = User.objects.filter(email__iexact = user_email)
            
            if user.exists():
                data = {"error":"User with the given email address already exists"}
                return Response(data, status = status.HTTP_400_BAD_REQUEST)
            else:
                is_valid = validate_email(user_email,verify=True)
                if is_valid:
                    serializer  = UserSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({"details":"This email does not exist. Please enter a valid email."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {"error":"Please enter valid email address."}
            return Response(data, status = status.HTTP_400_BAD_REQUEST)
