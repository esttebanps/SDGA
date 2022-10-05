from profiles.models import Administrator
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import DataUser,Supplier,Client

class AdministratorSerializer(serializers.ModelSerializer):
    email    = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = Administrator
        fields = ('email','username','password')
    
    def validate_password(self, value):
        return make_password(value)

class ClientSerializer(serializers.ModelSerializer):
    pass

class SupplierSerializer(serializers.ModelSerializer):
    pass
    

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'