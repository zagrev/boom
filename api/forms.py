from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class StreamForm(forms.Form):
    remote = forms.URLField(help_text='Remote URI of file to retrieve')
    file_name = forms.CharField(help_text='Valid file name including extension to name download')
    base64_encode = forms.ChoiceField(
        choices=(
            (True, "Base64 encode download"),
            (False, "Leave download unaltered")
        ),
        widget=forms.RadioSelect,
        initial=False)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        'remote',
        'file_name',
        'base64_encode',
        Submit('submit', 'Download', css_class='btn-primary'),
    )

class EmailForm(forms.Form):
    remote = forms.URLField(label='Remote URI of file to retrieve')
    file_name = forms.CharField(label='Valid file name with extension to name download')
    email = forms.EmailField(label='Email to send file')
    base64_encode = forms.BooleanField(label='Should it be base64 encoded', required=False)
