from rest_framework import generic, permissions
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import response
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.al()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthicated]

    def get_object(self):
        return self.request.user
