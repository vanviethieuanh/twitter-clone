from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from json import loads

from django.contrib.auth.models import User

from server.validators import validate_register

# Create your views here.

class Register(APIView):
    def post(self, request):
        data = request.body
        data = loads(data)

        validate_register(data)
        
        l_name      = data['last_name']
        f_name      = data['first_name']
        password    = data['password']
        email       = data['email']
 
        user = User.objects.create_user(email,email,password)
        user.last_name = l_name
        user.first_name = f_name
        user.save()

        return Response(self.get_tokens_for_user(user))

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


