from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.shortcuts import redirect
from django.conf import settings


class Registration(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration.html'

    def get(self, request):
        data = {"title": "Registration"}
        return Response(data=data)

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        hashed_password = make_password(password)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address already registered.")
        else:
            User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email, password=hashed_password).save()
            messages.success(request, "Welcome to Weather application !!! Please, Login with your creadentials.")
        return redirect('/')


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        data = {"title": "Login"}
        return Response(data=data)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = {}
        if User.objects.filter(email=email).exists():
            user= User.objects.get(email=email)
            if check_password(password, user.password):
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Wrong password.')    
        else:
            messages.error(request, 'Email not registered.')
        return redirect('/')


class Logout(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')
