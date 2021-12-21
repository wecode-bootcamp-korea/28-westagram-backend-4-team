import json
import re

from django.views           import View
from django.http            import JsonResponse, Http404
from django.db.utils        import IntegrityError
from django.core.exceptions import (PermissionDenied,
                                    EmptyResultSet)
from users.models           import User
from users.validator        import (validate_password,
                                   validate_email)

from westagram.checkitem    import CheckItem

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            signup_key_list=['username', 'email', 'password',]
            CheckItem.check_keys_in_body(data, signup_key_list)

            username     = data.get('username')
            email        = data.get('email')
            password     = data.get('password')
            phone_number = data.get('phone_number')
            
            validate_email(email)
            validate_password(password)

            if User.objects.filter(email_address=email).exists():
                raise IntegrityError("EMAIL_DUPLICATED_ERROR")
            
            user = User.objects.create(
                        username      = username,
                        password      = password,
                        email_address = email,
                        phone_number  = phone_number,
            )

            return JsonResponse({"message":"SUCCESS"}, status=201)
        
        except KeyError as e:
            return JsonResponse({"message":str(e)}, status=400)

        except IntegrityError as e:
            return JsonResponse({"message":str(e)}, status=409)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            signin_key_list=["email", "password"]
            CheckItem.check_keys_in_body(data, signin_key_list)

            email    = data.get("email")
            password = data.get("password")

            user = User.objects.filter(email_address=email)
            
            if not user.exists():
                raise EmptyResultSet("INVALID_USER")

            if user[0].password != password:
                raise PermissionDenied("INVALID_USER")

            return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError as e:
            return JsonResponse({"message":str(e)}, status=400)

        except EmptyResultSet as e:
            return JsonResponse({"message":str(e)}, status=401)

        except PermissionDenied as e:
            return JsonResponse({"message":str(e)}, status=401)
