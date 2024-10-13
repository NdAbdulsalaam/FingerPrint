# Generated by Django 5.1.1 on 2024-10-13 17:13

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_alter_participant_fingerprint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='fingerprint',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='participants'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='fingerprint',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='volunteers'),
        ),
    ]
