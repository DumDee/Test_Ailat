from django.contrib import admin
from .models import UserSubscription


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'source', 'is_active', 'activated_at', 'expires_at')
    search_fields = ('user__username', 'user__email')
    list_filter = ('plan', 'source', 'is_active')
