from django.db import models

# models here.
class User(models.Model):
    full_name     = models.CharField(max_length = 50)                   # 이름
    email         = models.CharField(max_length = 100)                  # 이메일
    password      = models.CharField(max_length = 300)                  # 비밀번호 (8~20자)
    mobile_number = models.CharField(max_length = 50, null = True)      # 전화번호 (-를 포함한 숫자)
    username      = models.CharField(max_length = 50)                   # 사용자 이름
    birth_date    = models.DateField(null =  True)                      # 생년월일

    class Meta:
        db_table = 'users'
    