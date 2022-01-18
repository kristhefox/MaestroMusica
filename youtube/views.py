import string, random
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Video, Comment


class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        
        recent_video = Video.objects.order_by('-datetime')[:10]

        return render(request, self.template_name, {'menu_item': 'home', 'recent_video': recent_video})


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
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/register')
        
        form = NewVideoForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = NewVideoForm(request.POST, request.FILES)
        

        if form.is_valid():
            # new video
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']  

            random_characters = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))      
            path = random_characters+file.name

            new_video = Video(title=title, description=description, user=request.user, path=path)
            new_video.save()

            return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:
            return HttpResponse('Form is invalid')