# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInformation(models.Model):
    username = models.CharField(max_length=4000,default="None",unique=True)
    address = models.CharField(max_length=4000,default="None")
    city = models.CharField(max_length=4000,default="None")
    zcode = models.CharField(max_length=4000,default="None")
    email = models.CharField(max_length=4000,default="None")
    phone = models.CharField(max_length=4000,default="None")
    application = models.CharField(max_length=4000,default="None")
    published_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

# ^^ Useable example table ^^


