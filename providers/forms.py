from django import forms
from providers.models import Provider
from django.forms.widgets import DateInput


class ProviderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    account_created = forms.DateField(
        widget=forms.DateInput(attrs=dict(type='date')))

    class Meta:
        model = Provider
        fields = ('name', 'address', 'code',
                  'password', 'email', 'account_created')
