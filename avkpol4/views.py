from django.shortcuts import render, redirect,  render_to_response, get_object_or_404, RequestContext
from django.forms import  ModelForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.views.generic.list  import BaseListView
from django.conf import settings
from django.views.generic.edit import UpdateView, FormView
import urllib2 # Used to download images
import cStringIO # Used to imitate reading from byte file
from PIL import Image # Holds downloaded image and verifies it
import copy # Copies instances of Image
import os
from django.forms.models import model_to_dict
from settings import common
import subprocess
from subprocess import Popen
import json
import requests

from forms import User_data_form
from models import UserData, RequestLog
from custom_middleware import last_10

def user_data_view(request):
    init_data = subprocess.Popen('python manage.py loaddata --app=avkpol4 mydata.old.json', shell=True)
    Popen.wait(init_data)
    model_values = UserData.objects.order_by('last_name')[0]

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
       }

    return render(request, 'home.html', context)

def get_from_request(request):
    #
    # instance = get_object_or_404(UserData, id=user_id)
    # form = User_data_form(request.POST or None, instance=instance)
    # if form.is_valid():
    #     form.save()
    #     return redirect('next_view', id=user_id)
    # return render_to_response(request, 'my_template.html', {'form': form})

    # model_values = UserData.objects.order_by('user_id')[0]
    # initial = model_values.id
    # if model_values.user_id == int(initial):
    #      if request.POST:
    #         edit_form = User_data_form(request.POST)
    #
    #         if edit_form.is_valid():
    #
    #             user_data = UserData.objects.get(pk=user_id)
    #             edit_form = User_data_form(request.POST, instance = user_data)
    #             edit_form.save()
    #             return redirect('/entry/1/edit', pk=edit_form.pk )
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
    # return user_model
    #     # edited_data = json.dumps(response_data, sort_keys = False, indent = 4)
    #
    #     user_model.save()
            # edited_data = UserData.objects.create(response_data)
            # if data.is_valid():
            #     data.save()
            # edited_data = json.dumps(response_data, sort_keys = False, indent = 4)
            # with open('mydata_edited.json', 'w') as output_file:
            #     output_file.write(edited_data)

                # return HttpResponse("Data sent")

    # except KeyError:
    #     raise("there are empty fields in form")

def user_edit(request):
    usr = UserData.objects.all()[0]
    if request.POST:
        form = User_data_form(request.POST, request.FILES, instance=usr)
        if form.is_valid():
            usr = form.save(commit=False)

            usr.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)



class UserEdit(FormView):

    def __init__(self, *args, **kwargs):
        super(UserEdit, self).__init__(*args, **kwargs)
        self.initial = model_to_dict(UserData.objects.first())

    form_class = User_data_form
    template_name = 'user_edit.html'

    def get_success_url(self):
        self.url = 'http://127.0.0.1:8000/edit'
        # self.url = self.object.get_absolute_url()
        return self.url

    # def get(self, request, **kwargs):
    #     print "hhhhhhhhh"
    #     return self.render_to_response(self.get_context_data(), **kwargs)
    def get_context_data(self, **kwargs):
        # img = UserData.objects.first().photo
        # # qs = UserData.objects.first().get_absolute_url(pk)


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



#
# class UserUpdateView(UpdateView):
#
#     model = UserData
#     template_name = 'user_edit.html'
#     form_class = UserUpdateForm
#     # photo = get_object_or_404(UserData, pk=1)
#     # photo = image
#     # print photo
#     # print image

        # return u'%s?status_message= Records successfully saved!'% ('home')
#
#     def post(self, request, *args, **kwargs):
#         if request.POST.get('cancel_button'):
#             return HttpResponseRedirect(
#                 u'%s?status_message=editing cancelled!'
#                 % reverse('home'))
#         else:
#             return super(UserUpdateView, self).post(request, *args, **kwargs)




# def save_image_from_url(url):
#
#     r = requests.get(url)
#     print r
#     img_temp = NamedTemporaryFile(delete=True)
#     img_temp.write(r.content)
#     img_temp.flush()
#
#     model.image.save("image.jpg", File(img_temp), save=True)

# def save_image_in_field(modelfield, url='',data=None,relativefile='',filename=None):
#     ''' Takes a model field of that model and a optional url or a filename
#     and saves the image to that field.
#     The url must be absolute
#     The filename is relative to the firsr static dir, using Unix style slashes /
#     The field must be a DjangoImageField'''
#
#     # if url and relativefile:
#     #     raise UserWarning('Function save_image_in_field expects a URL or a Filename not both.')
#     #
#     # if not filename:
#     #     filename = url.split('/')[-1]
#
#     if url:
#         r = requests.get(url)
#         data = r.content
#         if data is not None:
#
#
#             img_temp = NamedTemporaryFile(delete=True)
#             img_temp.write(data)
#             img_temp.flush()
#
#             modelfield.save(data, File(img_temp), save=True)
#             print data
#             return HttpResponseRedirect(reverse('user_edit'))
#

# def upload_photo(request):
#     # if request.method == 'POST':
#     form = UserUpdateForm(request.POST, request.FILES)
#     if form.is_valid():
#         image = UserData.objects.order_by('last_name')[0]
#         image.photo = form.cleaned_data['photo']
#         image.save()
#         # print image
#
#         return image

