from django import forms
from passports.models import Passport


class PassportTimeForm(forms.ModelForm):

    class Meta:
        model = Passport
        widgets = {
            'date_administered': forms.DateInput(attrs={'class': 'datepicker'}),
        }
