from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate, login

def login_page(request):
    return render(request, 'login.html')
    
def register_page(request):
    return render(request, 'register.html')