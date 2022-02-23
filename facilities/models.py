from django.db import models
from providers.models import Provider
# Create your models here.


class Facility(models.Model):

    name = models.CharField(max_length=50, blank=False,
                            default='', unique=True)
    address = models.CharField(max_length=50, blank=False, default='')
    code = models.CharField(max_length=50, blank=False,
                            default='', unique=True)
    password = models.CharField(blank=False, max_length=50)
    account_created = models.DateField(auto_now_add=True)
    email = models.EmailField(default='', unique=True)
    providers = models.ManyToManyField(Provider)

    class Meta:
        ordering = ['name', 'address', 'code']

    def __str__(self):
        return self.name
