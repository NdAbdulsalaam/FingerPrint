from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import Volunteer

# User = get_user_model()

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
    
    def create(self, validated_data):
        if 'fingerprint' not in validated_data or not validated_data['fingerprint']:
            validated_data['fingerprint'] = 'default_images/default_fingerprint.jpg'
        volunteer = Volunteer(**validated_data)
        volunteer.save()


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=30)
    subject = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=2000)

