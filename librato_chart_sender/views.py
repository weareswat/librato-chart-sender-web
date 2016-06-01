from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.template import Template

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))