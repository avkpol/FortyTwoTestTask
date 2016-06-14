from crispy_forms.bootstrap import FormActions
from django import forms

from models import UserData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML, Field
from crispy_forms import layout

"""
parent class for both UserDataForm and InitialForm
"""
class FormMixin(forms.ModelForm):


    class Meta:
        model = UserData
        fields = ['name', 'last_name', 'birth_date', 'bio', 'email', 'jabber', 'skype', 'photo', 'other_conts']

    def __init__(self, *args, **kwargs):
        super(FormMixin, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'data-fields'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('name',
                    'last_name',
                    'birth_date',
                    'photo',
                        HTML('<img src="{% if {{ url_photo }}" id="photo-preview">'),
                    css_class='col-md-6'),
                Div( 'email', 'jabber', 'skype', 'bio', 'other_conts', css_class='col-md-6'),
                    css_class='row-fluid'),
                Div(FormActions(Submit('save_changes', 'Save', css_class='col-md-6 btn btn-success pull-right')),
                css_class='row'),
            )

"""
editable form
"""
class UserDataForm(FormMixin):

    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)


class InitialForm(FormMixin):

    class Meta:
        model = UserData
        exclude = ['photo']

    def __init__(self, *args, **kwargs):
        super(InitialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.layout = Layout(
        Div(
            Div('name',
                'last_name',
                'birth_date',
                'bio',
                css_class='col-md-6'),
            Div( 'email', 'jabber', 'skype', 'other_conts', css_class='col-md-6'),
                css_class='row-fluid'),
        )



