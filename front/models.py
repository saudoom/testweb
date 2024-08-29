from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils import timezone
# Create your models here.
class CustomUser(AbstractUser):
    pass
class S_achievement(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    postdate=models.DateField(auto_now_add=True)
    picture=models.ImageField(upload_to='media')
class en_word(models.Model):
    spell=models.CharField(max_length=50)
    rank=models.CharField(max_length=4,choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')))
