from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    phonenumber = models.IntegerField()
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = "users"    
    
   
