from django.db import models

# Create your models here.
class Users(models.Model):
    user_name     = models.CharField(max_length=45)
    password      = models.CharField(max_length=50)
    email         = models.CharField(max_length=300, null=True)
    phone_number  = models.CharField(max_length=50, null=True)
    profile_image = models.CharField(max_length=300, blank=True) 
    profile_desc  = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "users"
