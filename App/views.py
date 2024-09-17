from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from .serializers import VolunteerSerializer, ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddVolunteerView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'add-volunteer.html')

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'matric_number': request.POST.get('matric_number'),
            'institution': request.POST.get('institution'),
            'faculty': request.POST.get('faculty'),
            'department': request.POST.get('department'),
            # 'fingerprint': request.FILES.get('fingerprint')
        }
        serializer = VolunteerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('success')
        else: 
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'add-volunteer.html', {'errors': errors})

    
class SuccessView(APIView):
    def get(self, request):
        return render(request, "success.html")
    
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