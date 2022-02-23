from django.db import models
# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    username = models.CharField(
        max_length=50, blank=False, default='', unique=True)
    password = models.CharField(blank=False, max_length=50)
    address = models.CharField(max_length=50, blank=False, default='')
    birthdate = models.DateField(blank=False, default='')
    email = models.EmailField(blank=False, unique=True, default='')
    date_joined = models.DateField(auto_now_add=True)
    # gender = models.CharField(blank=False, max_length=50)

    class Meta:
        ordering = ['first_name', 'last_name',
                    'username', 'address', 'birthdate', 'email']

    def __str__(self):
        return self.username
