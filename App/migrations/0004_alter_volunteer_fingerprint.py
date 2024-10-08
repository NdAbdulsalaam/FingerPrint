# Generated by Django 5.0.7 on 2024-09-16 16:42

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_volunteer_fingerprint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='fingerprint',
            field=imagekit.models.fields.ProcessedImageField(default='default_images/default_fingerprint.jpg', upload_to='fingerprints/'),
        ),
    ]
