from ..serializers import UserSerializer
from ..models import User

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import permissions
from rest_framework import response
from rest_framework import status
from rest_framework import views

from rest_framework.decorators import api_view


class UserInfoView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user, _ = JWTAuthentication().authenticate(request=request)
        return response.Response(UserSerializer(user).data)


@api_view(['GET'])
def check_used_email(request):
    email = request.query_params.get('email')
    if not email:
        return response.Response({'error': 'Email not provided!'}, status=status.HTTP_400_BAD_REQUEST)

    return response.Response({"isTaken": User.objects.filter(username=email['email']).exists()})
