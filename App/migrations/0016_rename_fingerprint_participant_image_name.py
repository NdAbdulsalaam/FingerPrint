# Generated by Django 5.1.1 on 2024-10-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_participant_image_alter_participant_fingerprint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='fingerprint',
            new_name='image_name',
        ),
    ]
