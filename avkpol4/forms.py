from crispy_forms.bootstrap import FormActions
from django import forms

from models import UserData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML

from floppyforms import ClearableFileInput

#
# class ImageThumbnailFileInput(ClearableFileInput):
#     template_name = 'image_thumbnail.html'


class User_data_form(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'last_name', 'birth_date', 'bio', 'email', 'jabber','skype', 'photo']


    def __init__(self, *args, **kwargs):
        super(User_data_form, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_id = 'data-fields'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('name', 'last_name', 'birth_date','email', 'jabber','skype', css_class='col-md-6'),
                Div('bio', 'photo', css_class='row'),
                HTML('<img src="{{ url_photo }}" id="photo-preview">'),

            ),
            FormActions(
            Submit('save_changes', 'Save', css_class="btn btn-primary"),
            Submit('cancel', 'Cancel', css_class='btn btn-default', type="button"),
            )

        )
