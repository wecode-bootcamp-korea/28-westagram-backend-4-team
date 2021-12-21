from django.shortcuts import render

import json

from django.http     import JsonResponse
from django.views    import View

from users.models import User
from users.validators import confirm_email, confirm_password

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not confirm_email(data['email']):
                return JsonResponse({'message' : 'impossible email'}, status=400)
            
            if not confirm_password(data['password']):
                return JsonResponse({'message' : 'impossible password'}, status=400)
            
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'email exists'}, status=400)

        
            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = data['password'],
                phonenumber = data['phonenumber'],
                gender      = data['gender'],
            )

            return JsonResponse({'message' : 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message' : 'KeyError'}, status=400)