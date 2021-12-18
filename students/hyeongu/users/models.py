from django.db import models

class User(models.Model):
    full_name     = models.CharField(max_length = 50)
    email         = models.CharField(max_length = 100, unique = True)
    password      = models.CharField(max_length = 300)
    mobile_number = models.CharField(max_length = 50, null = True)
    username      = models.CharField(max_length = 50, unique = True)
    birth_date    = models.DateField(null = True)
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
