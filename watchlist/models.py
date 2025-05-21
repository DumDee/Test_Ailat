from django.db import models
from django.conf import settings

#Акции отслеживаемые пользователем
class WatchedStock(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watched_stocks')
    stock = models.ForeignKey('stocks.Stock', on_delete=models.CASCADE, related_name='watchlisted_by')
    notifications_enabled = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'stock')
        ordering = ['-added_at']
        verbose_name = "Отслеживаемая акция"
        verbose_name_plural = "Отслеживаемые акции"

    def __str__(self):
        return f"{self.user} → {self.stock}"
