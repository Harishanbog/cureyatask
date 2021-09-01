from math import trunc
from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.contrib.auth.models import User,auth
import random


# Create your models here.
 
class userdetails(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    randomid=models.IntegerField(unique=True,default=0)
    number=models.BigIntegerField()
    type=models.CharField(max_length=10)
    mobile_otp=models.IntegerField(default=0)
    email_otp=models.IntegerField(default=0)


    def userdetails(self):
        pass
    def __str__(self):
        return f"{self.user.first_name} {self.type} {self.randomid}"