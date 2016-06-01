from django.contrib import admin
from models import UserData, RequestLog, ModelLog

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birth_date', 'email', 'jabber', 'skype',)

admin.site.register(UserData, UserAdmin)
admin.site.register(RequestLog)
admin.site.register(ModelLog)
