from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(forms.ModelForm):
    delete_user = forms.BooleanField(required=False, label='Удалить пользователя')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)  # Укажите необходимые поля

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password')