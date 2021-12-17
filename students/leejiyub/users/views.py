from django.shortcuts import render


import json

from django.http     import JsonResponse
from django.views    import View

from users.models import User


class UsersView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.create(
            name        =data['user_name'],
            email       = data['user_email'],
            password    = data['user_password'],
            phonenumber = data['user_phonenumber'],
            gender      = data['user_gender'],
        )