from crispy_forms.bootstrap import FormActions
from django import forms

from models import UserData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Button, Div, HTML


class FormMixin(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'last_name', 'birth_date', 'bio', 'email', 'jabber','skype', 'photo']

    def __init__(self, *args, **kwargs):
        super(FormMixin, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_id = 'data-fields'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('name', 'last_name', 'birth_date','email', 'jabber','skype','bio', css_class='col-md-6'),
                Div('photo', css_class='col-md-6'),
                HTML('<img src="{{ url_photo }}" id="photo-preview" class="pull-right form-inline">'),
            FormActions(Submit('save_changes', 'Save', css_class='btn btn-success'),)
            )
        )

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



