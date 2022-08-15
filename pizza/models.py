from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from rest_framework.authtoken.models import Token
from django.conf import settings 



# Create your models here.
class customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=200,default="")
   
    def __str__(self):
        return self.user.username
class products(models.Model):
    name=models.CharField(max_length=200,default="")
    description=models.CharField(max_length=200,default="")
    price=models.DecimalField(max_digits=6,decimal_places=2,default=0.0)
    is_active=models.BooleanField(default=True)
    date=models.DateField(default=datetime.now)
    def __str__(self):
        return self.name

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    body=models.TextField()

#@receiver(post_save,sender=settings.AUTH_USER_MODEL)
#def getToken(sender,instance,created,**kwargs):
    #if created:
        #Token.objects.create(user=instance)

   



    

