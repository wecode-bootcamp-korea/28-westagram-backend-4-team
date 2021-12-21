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
            full_name = user_data['full_name']
            email     = user_data['email']
            password  = user_data['password']
            username  = user_data['username']
        
            if is_email_valid(email) == None:
                raise ValidationError('INVALID_EMAIL')

            elif is_password_valid(password) == None:
                raise ValidationError('INVALID_PASSWORD')

            elif User.objects.filter(email=email).exists():
                raise ValidationError('DUPLICATED_EMAIL')

            elif User.objects.filter(username=username).exists():
                raise ValidationError('DUPLICATED_USERNAME')

            else:
                if 'mobile_number' in user_data.keys():
                    mobile_number = user_data['mobile_number']
                else: 
                    mobile_number = None
                    
                if 'birth_date' in user_data.keys():
                    birth_date = user_data['brith_date']
                else:
                    birth_date = None

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