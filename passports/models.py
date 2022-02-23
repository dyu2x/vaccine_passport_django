from django.db import models
from providers.models import Provider
from facilities.models import Facility
from users.models import User
# Create your models here.


class Passport(models.Model):

    description = models.CharField(max_length=50, blank=False, default='')
    date_administered = models.DateField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
