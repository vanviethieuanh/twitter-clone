from authentication.serializers import UserSerializer

from rest_framework import response
from rest_framework import views
from rest_framework import permissions


class Register(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer = UserSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)

        return response.Response(UserSerializer(user).data)
