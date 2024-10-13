from django.db import models
import uuid
import os
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.core.exceptions import ValidationError

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
        upload_to='volunteers',
        processors=[ResizeToFit(300, 300)],
        options={'quality': 100}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class Participant(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, default=uuid.uuid4, editable=False)
    image = ProcessedImageField(
        upload_to='participants',
        processors=[ResizeToFit(300, 300)],
        options={'quality': 100},
    )
    image_name = models.CharField(max_length=255, blank=True, unique=True, editable=False)

    def clean(self):
        # Get the file name without the directory path
        if self.image:
            image_name = os.path.basename(self.image.name)
            # Check if another record already has this image name
            if Participant.objects.filter(image_name=image_name).exists():
                raise ValidationError(f"An image with the name '{image_name}' already exists.")
            self.image_name = image_name  # Set the field to match the image name
    
    def save(self, *args, **kwargs):
        # Perform the validation before saving
        self.clean()
        super(Participant, self).save(*args, **kwargs)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)