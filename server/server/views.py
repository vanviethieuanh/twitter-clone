from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from json import loads
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User

from server.validators import validate_register

# Create your views here.


def index(request):
    return render(request, 'index.html')


class Register(APIView):
    def post(self, request):
        data = request.body
        data = loads(data)

        validate_register(data)

        l_name = data['last_name']
        f_name = data['first_name']
        password = data['password']
        email = data['email']

        user = User.objects.create_user(email, email, password)
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


class isUsedEmail(APIView):
    def post(self, request):
        data = loads(request.body)
        return Response({"isTaken": User.objects.filter(username=data['email']).count()})
