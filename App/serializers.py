from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import Volunteer

# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        #fields = ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'gender', 'password1', 'password2')
    
    def create(self, validated_data):
        volunteer = Volunteer(**validated_data)
        volunteer.save()
        return volunteer


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=30)
    subject = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=2000)

