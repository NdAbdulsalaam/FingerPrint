from django.db import models
import uuid
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Volunteer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    matric_number = models.CharField(max_length=15)
    institution = models.CharField(max_length=8, choices=[
        ('UI', 'University of Ibadan'), 
        ('FSSOYO', 'Federal School of Surveying, Oyo'), 
        ('EAUEDOYO', 'Emmanuel Alayande University of Education, Oyo')
    ])
    faculty = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    fingerprint = ProcessedImageField(
        upload_to='fingerprints/volunteer',
        processors=[ResizeToFit(300, 300)],
        options={'quality': 100},
        default='fingerprints/default_fingerprint.jpg',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class Participant(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, default=uuid.uuid4, editable=False)
    fingerprint = ProcessedImageField(
        upload_to='fingerprints/participant',
        processors=[ResizeToFit(300, 300)],
        options={'quality': 100},
        default='fingerprints/default_fingerprint.jpg',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)