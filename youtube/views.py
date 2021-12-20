from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variable_a = 'Text'
        return render(request, self.template_name, {'variable_a':variable_a})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('POST!!!')
        return HttpResponse('Login. POST request')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
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
    template_name = 'new_video.html'

    def get(self, request):
        variable_a = 'New Video'
        form = FormClass()
        return render(request, self.template_name, {'variable_a':variable_a, 'form':form})


    def post(self, request):
        return HttpResponse('Index. POST request')