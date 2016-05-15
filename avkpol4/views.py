from django.shortcuts import render
import subprocess
from subprocess import Popen

from . forms import User_data_form
from . models import User_data
from . custom_middleware import last_10



def user_data_view(request):

    last_ten = last_10()


    init_data = subprocess.Popen('python manage.py loaddata --app=avkpol4 mydata.json', shell=True)
    Popen.wait(init_data)
    model_values = User_data.objects.get(id=1)

    form = User_data_form(initial={
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
        'last_ten':last_ten,
        }
    return render(request, 'home.html', context)



