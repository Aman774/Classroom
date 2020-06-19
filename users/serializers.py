from rest_framework import serializers
from . import models 

from django.contrib.auth.models import User




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'




class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    age =serializers.IntegerField(required=True)
    city=serializers.CharField(required=True)
    grade=serializers.CharField(required=True)
    board=serializers.CharField(required=True) 


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User class. Used to create new users.
    """

    #password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
        "first_name",
         "last_name",
          "email",
          "password",
        )






 


