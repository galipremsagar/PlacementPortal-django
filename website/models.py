from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Auth1(models.Model):
    pin_number = models.IntegerField()
    sessionKey = models.CharField(max_length=250)
    password = models.CharField(max_length=250,default="")

