from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class UserSubscription(models.Model):
    PLAN_CHOICES = [
        ('monthly', 'Ежемесячно'),
        ('yearly', 'Ежегодно'),
    ]

    SOURCE_CHOICES = [
        ('apple', 'Apple Store'),
        ('card', 'Банковская карта'),
        ('kaspi', 'Kaspi'),
        ('admin', 'Ручная активация')
    ]

    SUBSCRIPTION_TYPE = [
        ('pro', 'PRO'),
        ('plus', 'PLUS'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    type = models.CharField(max_length=10, choices=SUBSCRIPTION_TYPE, default='pro')
    is_active = models.BooleanField(default=True)
    activated_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.is_active = self.expires_at > timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Подписка пользователя"
        verbose_name_plural = "Подписки пользователей"

    def __str__(self):
        return f"{self.user.username} — {self.plan} ({'активна' if self.is_active else 'неактивна'})"
