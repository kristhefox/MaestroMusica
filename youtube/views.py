from django.shortcuts import render
from django.views.generic.base import View, HttpResponse


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        variable_a = 'Text'
        return render(request, self.template_name, {'variable_a':variable_a})


    def post(get, request):
        return HttpResponse('Index. POST request')

class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variable_a = 'New Video'
        return render(request, self.template_name, {'variable_a':variable_a})


    def post(get, request):
        return HttpResponse('Index. POST request')