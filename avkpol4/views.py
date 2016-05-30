from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.forms.models import model_to_dict
from settings import common
import subprocess
from subprocess import Popen
import json

from forms import UserDataForm, InitialForm
from models import UserData, RequestLog
from custom_middleware import last_10

def user_data_view(request):
    init_data = subprocess.Popen('python manage.py loaddata --app=avkpol4 mydata.old.json', shell=True)
    Popen.wait(init_data)
    model_values = UserData.objects.order_by('last_name')[0]

    form = InitialForm(initial={
        'name':model_values.name,
        'last_name':model_values.last_name,
        'birth_date':model_values.birth_date,
        'bio':model_values.bio,
        'email':model_values.email,
        'jabber':model_values.jabber,
        'skype':model_values.skype,
        })

    context = {
        'form':form,
       }

    return render(request, 'home.html', context)

def get_from_request(request):

    data = json.loads(request.body)
    response_data = {
        'name':data['name'],
        'last_name':data['last_name'],
        'birth_date':data['birth_date'],
        'bio':data['bio'],
        'email':data['email'],
        'jabber':data['jabber'],
        'skype':data['skype']
    }

    user_model = UserData(**response_data)
    user_model.save()

def user_edit(request):
    usr = UserData.objects.all()[0]
    if request.POST:
        form = UserDataForm(request.POST, request.FILES, instance=usr)
        if form.is_valid():
            usr = form.save(commit=False)

            usr.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)


class UserEdit(FormView):

    def __init__(self, *args, **kwargs):
        super(UserEdit, self).__init__(*args, **kwargs)
        self.initial = model_to_dict(UserData.objects.first())

    form_class = UserDataForm
    template_name = 'user_edit.html'

    def get_success_url(self):
        self.url = 'http://127.0.0.1:8000/edit'
        # self.url = self.object.get_absolute_url()
        return self.url

    def get_context_data(self, **kwargs):

        context = super(UserEdit, self).get_context_data(**kwargs)
        context['url_photo'] = common.MEDIA_URL + str(UserData.objects.first().photo)
        return context


def request_count(request):
    last_ten = last_10()
    requests = len(RequestLog.objects.all())
    context = {
        'requests':requests,
        'last_ten':last_ten
    }
    return render(request,'requests_log.html',context)


