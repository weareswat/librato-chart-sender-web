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
            error_list = {'error_list': form.get_errors()}
            error_list.update(form.get_form_values())
            return render(request, 'config/new.html', error_list)
    else:
        return render(request, 'config/new.html')

