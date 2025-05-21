from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    language = models.CharField(max_length=10, default='en')
    currency = models.CharField(max_length=10, default='USD')
    dark_mode = models.BooleanField(default=False)
    notifications_enabled = models.BooleanField(default=True)
    pin_code_hash = models.CharField(max_length=128, blank=True)
    face_id_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"Profile of {self.user.email}"
