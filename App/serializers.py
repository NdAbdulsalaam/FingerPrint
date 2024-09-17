from rest_framework import serializers
from .models import Volunteer


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
            
    def create(self, validated_data):
        volunteer = Volunteer(**validated_data)
        volunteer.save()
        return volunteer

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=30)
    subject = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=2000)

