from django import forms

from . models import User_data


class User_data_form(forms.ModelForm):
    class Meta:
        model = User_data
        fields = '__all__'