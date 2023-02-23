from django.db import models

# Create your models here.
class adminregdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    MOBILE = models.IntegerField(null=True, blank=True)
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile",null=True, blank=True)

class gallerydb(models.Model):
    TITLE = models.CharField(max_length=50, null=True, blank=True)
    NAME = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile", null=True, blank=True)

class pricingdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    PHOTOS = models.CharField(max_length=50, null=True, blank=True)
    CAMERA = models.CharField(max_length=50, null=True, blank=True)
    TERM = models.CharField(max_length=50, null=True, blank=True)
    PRICING = models.IntegerField(null=True, blank=True)
    # IMAGE = models.ImageField(upload_to="profile", null=True, blank=True)

class bookingdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    MOBILE = models.IntegerField(null=True, blank=True)
    DATE = models.DateField(max_length=50, null=True, blank=True)
    TYPE = models.CharField(max_length=50, null=True, blank=True)

class contactdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    SUBJECT = models.CharField(max_length=50, null=True, blank=True)
    MESSAGE = models.CharField(max_length=50, null=True, blank=True)