# Generated by Django 5.2 on 2025-05-22 12:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referral_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
