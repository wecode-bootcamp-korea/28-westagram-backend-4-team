import json

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

            if User.objects.filter(email=email).exists():
                raise ValidationError('DUPLICATED_EMAIL')

            if User.objects.filter(username=username).exists():
                raise ValidationError('DUPLICATED_USERNAME')

            User.objects.create(
                full_name     = full_name,
                email         = email,
                password      = password,
                username      = username,
                mobile_number = mobile_number,
                birth_date    = birth_date,
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({'message':e.message}, status=400)