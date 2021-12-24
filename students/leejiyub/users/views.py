from django.shortcuts import render

import json
import bcrypt
from django.http     import JsonResponse
from django.views    import View

from users.models import User
from users.validators import confirm_email, confirm_password

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            password = data['password']     
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if not confirm_email(data['email']):
                return JsonResponse({'message' : 'impossible email'}, status=400)
            
            if not confirm_password(data['password']):
                return JsonResponse({'message' : 'impossible password'}, status=400)
            
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'email exists'}, status=400)

        
            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = hashed_password,
                phonenumber = data['phonenumber'],
                gender      = data['gender'],
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message' : 'KeyError'}, status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
       
        try:
            email    = data['email']
            password = data['password']                

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            user = User.objects.get(email = email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'KeyError'}, status=400)

                



                




                


