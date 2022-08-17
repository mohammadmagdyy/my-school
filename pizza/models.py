from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from rest_framework.authtoken.models import Token
from django.conf import settings 



# Create your models here.
class students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=200,default="")
    reserved=models.BooleanField(default=False)
   
    def __str__(self):
        return self.user.username


#@receiver(post_save,sender=settings.AUTH_USER_MODEL)
#def getToken(sender,instance,created,**kwargs):
    #if created:
        #Token.objects.create(user=instance)

   



    

