from django import forms

from models import User_data


class User_data_form(forms.ModelForm):
    class Meta:
        model = User_data
        fields = '__all__'




class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()