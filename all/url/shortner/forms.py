from .validators import validate_url, validate_dot_com
from django import forms
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])