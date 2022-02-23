from django import forms
from users.models import User
from django.forms.widgets import DateInput


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs=dict(type='date')))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password', 'email', 'address', 'birthdate', 'account_created')
