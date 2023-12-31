import datetime
import logging

import jwt
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from HRManagement.settings import SECRET_KEY
from members.models import User
from members.permissions import login_required
from members.serializers import UserSerializer


@permission_classes((AllowAny,))
class RegisterView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        logging.log(level=logging.WARNING, msg=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)


@permission_classes((AllowAny,))
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if not user:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        token_payload = {
            'id': user.id,
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.UTC)
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
        response = JsonResponse({'status': 'success', 'message': 'Login successful'})
        response.set_cookie(key='jwt', value=token, httponly=True, expires=token_payload['exp'])
        return response


@login_required
def data(request):
    return JsonResponse({'status': 'success', 'message': request.COOKIES.get('jwt')}, status=200)

