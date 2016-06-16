from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import NewConfigForm
from django.shortcuts import redirect

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def config_new(request):
    if request.method == "POST":
        form = NewConfigForm(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            return render(request, 'config/new.html', { 'errors': form.errors})
    else:
        return render(request, 'config/new.html')

