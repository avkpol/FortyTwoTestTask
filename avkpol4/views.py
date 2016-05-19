from django.shortcuts import render
from django.forms import  ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView

import subprocess
from subprocess import Popen
import json

from forms import User_data_form, UploadFileForm
from models import User_data
from custom_middleware import last_10

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import FormActions

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

def get_from_request(request):
    try:
        if request.method == 'POST':

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
            edited_data = json.dumps(response_data, sort_keys = False, indent = 4)
            with open('mydata_edited.json', 'w') as output_file:
                output_file.write(edited_data)

                return HttpResponse("Data sent")

    except KeyError:
        print "there are empty fields in form"


class UserUpdateForm(ModelForm):
    class Meta:
        model = User_data
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('user_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline =True
        self.helper.html5_required =True
        self.helper.label_class = 'col-sm-6 control-label'
        self.helper.field_class = 'col-sm-10'

        # add fields
        self.helper.layout = Layout(
            Fieldset(
                '',
                'name',
                'last_name',
                'birth_date',
                'bio',
                'email',
                'jabber',
                'skype',
            ),
              # add buttons
            FormActions(
                Submit('add_button', u'Save',css_class = 'btn btn-primary'),
                Submit('cancel_button',u'Cancel', css_class ='btn btn-link'),
            )
        )
class UserUpdateView(UpdateView):
    model= User_data
    template_name = 'user_edit.html'
    form_class = UserUpdateForm

    def get_success_url(self):
        self.url = 'http://127.0.0.1:8000/entry/1/edit'
        return self.url
        # return u'%s?status_message= Records successfully saved!'% ('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=editing cancelled!'
                % reverse('home'))
        else:
            return super(UserUpdateView, self).post(request, *args, **kwargs)

