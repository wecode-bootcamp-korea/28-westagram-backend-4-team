import json
import re

from django.views      import View
from django.http       import JsonResponse, Http404
from users.models      import User
from users.check_items import (check_character_policy, 
                               check_dictionary_keys,
                               login_key_list,
                               password_policy,
                               email_policy)

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            check_dictionary_keys(data, login_key_list)

            username     = data['username']
            email        = data['email'] 
            password     = data['password']
            

            check_character_policy(password_policy, password)
            check_character_policy(email_policy, email)

            if(User.objects.filter(email_address=email).exists()):
                message = "EMAIL_EXISTS"
                status  = 409

            else:
                user = User.objects.create(
                        username      = username,
                        password      = password,
                        email_address = email,
                )
                if 'phone_number' in data:
                    user.phone_number = data['phone_number']
                    user.save()

                message = "SUCCESS"
                status  = 201

        except Exception as e:
            message = str(e)
            status  = 403

        return JsonResponse({"message":message}, status=status)
