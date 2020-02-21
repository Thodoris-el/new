from django import forms
from django.forms import ModelForm
from api.models import *

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ('loginname','password','firstname','lastname')
