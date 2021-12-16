from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=100)
    password = models.IntegerField()
    phonenumber = models.IntegerField()
    gender = models.CharField(max_length=100)

    class Meta:
        db_table = "users"    
    
   
