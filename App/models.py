from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Volunteer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    matric_number = models.CharField(max_length=15)
    institution = models.CharField(max_length=8, choices=[('UI', 'University of Ibadan'), ('FSSOYO', 'Federal School of Surveying, Oyo'), ('EAUEDOYO', 'Emmanuel Alayande University of Education, Oyo')])
    faculty = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    fingerprint = ProcessedImageField(
        upload_to='fingerprints/',
        processors=[ResizeToFit(300, 300)],
        format='JPEG',
        options={'quality': 90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
