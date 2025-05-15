from django.contrib import admin
from .models import WatchedStock


@admin.register(WatchedStock)
class WatchedStockAdmin(admin.ModelAdmin):
    list_display = ('user', 'stock', 'notifications_enabled', 'added_at')
    list_filter = ('notifications_enabled', 'added_at')
    search_fields = ('user__username', 'stock__ticker', 'stock__name')
    autocomplete_fields = ['user', 'stock']
