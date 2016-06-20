from django.shortcuts import render, get_object_or_404
from .forms import NewConfigForm
from django.shortcuts import redirect
from .models import Configuration


def index(request):
    configurations = Configuration.objects.all()
    return render(request, 'index.html', {'configurations': configurations})


def config_new(request):
    if request.method == "POST":
        form = NewConfigForm(request.POST)
        if form.is_valid():
            new_config = Configuration(librato_user = form.get_form_values()['email_username'],
                                       librato_api_key = form.get_form_values()['api_key'],
                                       recipients_emails = ','.join(form.get_form_values()['recipients']),
                                       chart_ids = ','.join(form.get_form_values()['chart_ids']),
                                       interval = 1,
                                       duration = 2,
                                       template = 'something to change')
            new_config.save()
            return redirect('index')
        else:
            error_list = {'error_list': form.get_errors()}
            error_list.update(form.get_form_values())
            return render(request, 'config/new.html', error_list)
    else:
        return render(request, 'config/new.html', {'title': 'New Config'})


def config_edit(request, config_id):
    config = Configuration.objects.get(id=config_id)
    email_username = config.librato_user
    api_key = config.librato_api_key
    recipients = config.recipients_emails.split(',')
    chart_ids = config.chart_ids.split(',')

    return render(request, 'config/new.html', {'title': 'Edit Config',
                                               'email_username': email_username,
                                               'api_key': api_key,
                                               'recipients': recipients,
                                               'chart_ids': chart_ids})