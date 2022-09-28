from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from profiles.models import Administrator

from profiles.serializers import AdministratorSerializer


class LoginView(APIView):
    queryset = Administrator.objects.all() 
    def post(self, request):
        
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                AdministratorSerializer(Administrator).data,
                status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)
  
        
class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    
class SignupView(generics.CreateAPIView):
    serializer_class = AdministratorSerializer
    
