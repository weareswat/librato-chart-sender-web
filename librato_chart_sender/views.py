from django.shortcuts import render, get_object_or_404
from .forms import NewConfigForm
from django.shortcuts import redirect
from .models import Configuration
from db.config_db import ConfigDB
from chart_sender import LibratoChartSender


def index(request):
    configurations = Configuration.objects.all()
    return render(request, 'index.html', {'configurations': configurations})


def config_new(request):
    if request.method == "POST":
        form = NewConfigForm(request.POST)
        if form.is_valid():
            ConfigDB.create_configuration(form.get_form_values())
            return redirect('index')
        else:
            error_list = {'error_list': form.get_errors()}
            error_list.update(form.get_form_values())
            error_list.update({'title': 'New Config',
                               'page': 'new',
                               'available_options': ['daily', 'weekly', 'monthly']})
            return render(request, 'config/new.html', error_list)
    else:
        return render(request, 'config/new.html', {'title': 'New Config',
                                                   'page': 'new',
                                                   'duration': '604800',
                                                   'interval': 'weekly',
                                                   'available_options': ['daily', 'weekly', 'monthly']})


def config_edit(request, config_id):
    config = Configuration.objects.get(id=config_id)
    if request.method == "POST":
        form = NewConfigForm(request.POST)
        if form.is_valid():
            ConfigDB.update_configuration(config_id, form.get_form_values())
            return redirect('index')
        else:
            error_list = {'error_list': form.get_errors()}
            error_list.update(form.get_form_values())
            error_list.update({'title': 'New Config',
                               'page': 'new',
                               'available_options': ['daily', 'weekly', 'monthly']})
            return render(request, 'config/new.html', error_list)
    else:
        return render(request, 'config/new.html', {'title': 'Edit Config',
                                                   'page': 'edit/' + config_id,
                                                   'email_username': config.librato_user,
                                                   'api_key': config.librato_api_key,
                                                   'recipients': config.recipients_emails,
                                                   'chart_ids': config.chart_ids,
                                                   'duration': config.duration,
                                                   'available_options': ['daily', 'weekly', 'monthly'],
                                                   'interval': config.interval})


def config_delete(request, config_id):
    ConfigDB.delete_configuration(config_id)
    return redirect('index')

def send_now(request, config_id):
    chart_sender = LibratoChartSender([3419, 3420, 3421], ['pawel.krysiak@rupeal.com'], {
        'librato_api_key': 'b4bf0341c8cdd3b429826a18d1a07582895fa12c7fb97eb8f2c6bdb015004b86',
        'mailgun_api_key': 'key-a05af654983f6c57ec99904a3b84c7b3'})
    chart_sender.run()
    return redirect('index')