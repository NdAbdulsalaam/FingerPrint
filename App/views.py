from rest_framework import viewsets, generics
from .models import User, Participant
from .serializers import UserSerializer, ParticipantSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import JsonResponse
from .serializers import UserSerializer, LoginSerializer, UserProfileSerializer, ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.template.loader import render_to_string

class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class UserRegistrationView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'date_of_birth': request.POST.get('date_of_birth'),
            'gender': request.POST.get('gender'),
            'password1': request.POST.get('password1'),
            'password2': request.POST.get('password2'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('user-login')
        else: 
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'register.html', {'errors': errors})
    
class UserLoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return redirect('user-profile')  # Change this to the name of your dashboard URL
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'login.html', {'errors': errors})

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return render(request, 'profile.html', {'serializer': serializer, 'user': user})

    def post(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('user-profile')
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'profile.html', {'serializer': serializer, 'user': user, 'errors': errors})
        
@login_required
def user_logout(request):
    logout(request)
    return redirect('user-login')

class ContactView(APIView):
    def get(self, request):
        return render(request, "contact.html")
    
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            
            # Create the email
            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email=name,
                to=[settings.EMAIL_HOST_USER],
                headers={'Reply-To': email}
            )
            
            # Send the email
            email_message.send(fail_silently=False)
            
            return Response({"message": "Your message has been sent successfully."}, status=status.HTTP_200_OK)
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return JsonResponse({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

