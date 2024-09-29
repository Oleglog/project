from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)