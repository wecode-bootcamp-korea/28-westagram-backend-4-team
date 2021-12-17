from django.db import models


class User(models.Model):
    username      = models.CharField(max_length=45)
    password      = models.CharField(max_length=256)
    email_address = models.CharField(max_length=300, unique=True)
    phone_number  = models.CharField(max_length=50, null=True)
    profile_image = models.CharField(max_length=300, blank=True) 
    profile_bio   = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "users"
