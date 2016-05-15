from django.contrib import admin

from . models import User_data
from . request_model import RequestLog



admin.site.register(User_data)
admin.site.register(RequestLog)
