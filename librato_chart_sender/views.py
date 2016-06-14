from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.template import Template

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


def config_new(request):
    if request.method == "GET":
        return render(request, 'config/new.html')
    else:
        return render(request, 'config/temp.html')

