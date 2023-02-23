from django.db import models

# Create your models here.

class logindb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.IntegerField(null=True, blank=True)
    CONFIRMPASSWORD = models.IntegerField( null=True, blank=True)