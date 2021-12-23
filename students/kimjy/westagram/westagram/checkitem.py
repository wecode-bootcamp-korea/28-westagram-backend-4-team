import jwt
import datetime

from django.http import JsonResponse
from django.conf import settings
class CheckItem:
    def check_keys_in_body(check_dict:dict, necessary_key_list:list):

        check_dict_keys = check_dict.keys()
    
        if not set(necessary_key_list).issubset(set(check_dict_keys)):
            required_keys = set(necessary_key_list) \
                          - set(necessary_key_list).intersection(set(check_dict_keys))

            error_message='' 
            for required_key in required_keys:
                error_message += required_key + ", "

            raise KeyError(f"[{error_message}] was not found in http body")

    def check_jwt(func):
        def wrapper(self, request, *args, **kwargs):
            try:
                token = request.headers.get("Authorization", None)

                if token:
                    token_payload = jwt.decode(
                            token, 
                            settings.SECRET_KEY, 
                            algorithms=settings.ALGORITHM,
                    )

                    user_id  = token_payload['id']
                    return func(self, request, user_id=user_id)

                else:
                    return JsonResponse({'message':'token was not found'}, status=400)

            except KeyError as e:
                return JsonResponse({'message': getattr(e,'message',str(e))},status=401)
            
            except jwt.ExpiredSignatureError:
                return JsonResponse({'message':'TOKEN_EXPIRED'}, status=400)

        return wrapper
