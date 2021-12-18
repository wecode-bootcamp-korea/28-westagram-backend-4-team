from django.db import models


class User(models.Model):
    name        = models.CharField(max_length=40)
    email       = models.CharField(max_length=100)
    password    = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=40)
    gender      = models.CharField(max_length=10)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "users"    
    
   
