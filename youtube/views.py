from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        variable_a = 'Text'
        return render(request, self.template_name, {'variable_a':variable_a})


class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect('/')
            
        else:
            form = LoginForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('login')
        return HttpResponse('Login. POST request')


class RegisterView(View):
    template_name = 'register.html'
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            form = RegisterForm()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # creating user account
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            account = User(username=username, email=email)
            account.set_password(password)
            account.save()
            return HttpResponseRedirect('/login')
        return HttpResponse('Register. POST request')


class NewVideo(View):
    template_name = 'new-video.html'
    def get(self, request):
        variable_a = 'New Video'
        form = NewVideoForm()
        return render(request, self.template_name, {'variable_a':variable_a, 'form':form})

    def post(self, request):
        return HttpResponse('Index. POST request')