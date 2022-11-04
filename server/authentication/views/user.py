from authentication.serializers import UserSerializer
from authentication.models import User

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import permissions
from rest_framework import response
from rest_framework import exceptions
from rest_framework import views

from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from common.helpers.doc import EmailQueryParameter


class UserView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer = UserSerializer

    @swagger_auto_schema(
        operation_summary="Register new user.",
        request_body=UserSerializer
    )
    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create()

        return response.Response(self.serializer(user).data)


class UserInfoView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Return user infomation associate with the token."
    )
    def get(self, request):
        user = request.user
        return response.Response(self.serializer(user).data)


@swagger_auto_schema(
    method='get',
    operation_summary="Check whatever an email is used by another user.",
    manual_parameters=[
        EmailQueryParameter(description='Email to check.', required=True)
    ]
)
@api_view(['GET'])
def check_used_email(request):
    email = request.query_params.get('email')
    if not email:
        raise exceptions.NotAcceptable(detail="Email is require.")

    is_taken = User.objects.filter(email=email).exists()

    return response.Response({"isTaken": is_taken})
