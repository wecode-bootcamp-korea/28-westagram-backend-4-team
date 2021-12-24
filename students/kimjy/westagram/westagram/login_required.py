import jwt

from users.views import User
from django.http import JsonResponse
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM  = settings.ALGORITHM

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization", None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id=payload.get('id'))
            request.user= user
            return func(self, request)
        except KeyError as e:
            return JsonResponse({'message': getattr(e,'message',str(e))},status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message':'TOKEN_EXPIRED'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=400)

    return wrapper
