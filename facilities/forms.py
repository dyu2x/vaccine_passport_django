from django import forms
from facilities.models import Facility
from django.forms.widgets import DateInput


class FacilityForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Facility
        fields = ('name', 'code', 'address', 'password',
                  'email', 'account_created')
