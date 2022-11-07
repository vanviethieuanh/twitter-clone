from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import AuthTokenObtainPairSerializer

class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer
