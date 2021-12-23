import json
import bcrypt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models      import User
from .validations import is_email_valid, is_password_valid

class SignUpView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        
        try:
            full_name     = user_data['full_name']
            email         = user_data['email']
            password      = user_data['password']
            username      = user_data['username']
            mobile_number = user_data.get('mobile_number', None)
            birth_date    = user_data.get('birth_date', None)
        
            if not is_email_valid(email):
                raise ValidationError('INVALID_EMAIL')

            if not is_password_valid(password):
                raise ValidationError('INVALID_PASSWORD')

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if User.objects.filter(email=email).exists():
                raise ValidationError('DUPLICATED_EMAIL')

            if User.objects.filter(username=username).exists():
                raise ValidationError('DUPLICATED_USERNAME')

            User.objects.create(
                full_name     = full_name,
                email         = email,
                password      = hashed_password,
                username      = username,
                mobile_number = mobile_number,
                birth_date    = birth_date,
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':e.message}, status=400)

class LogInView(View):
    def post(self, request):
        try:
            login_data    = json.loads(request.body)

            email         = login_data['email']
            password      = login_data['password']

            if not User.objects.filter(email = email).exists():
                raise ValidationError('INVALID_USER')

            hashed_password = User.objects.get(email=email).password.encode('utf-8')

            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                raise ValidationError('INVALID_USER')

            return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({"message":e.message}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status=401)