import logging
import jwt
from rest_framework.exceptions import AuthenticationFailed
from HRManagement.settings import SECRET_KEY


def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        jwt_token = request.COOKIES.get('jwt')
        if not jwt_token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        logging.log(level=logging.WARNING, msg='in return view func')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
