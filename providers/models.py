from django.db import models
import datetime
# Create your models here.


class Provider(models.Model):

    name = models.CharField(max_length=50, blank=False,
                            default='', unique=True)
    code = models.CharField(max_length=50, blank=False,
                            default='', unique=True)
    password = models.CharField(blank=False, max_length=50)
    address = models.CharField(max_length=50, blank=False, default='')
    email = models.EmailField(default='', unique=True)
    join_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name', 'code', 'address', 'join_date', 'email']

    def __str__(self):
        return self.name
