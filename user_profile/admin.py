from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'currency', 'face_id_enabled', 'dark_mode')
    search_fields = ('user__username', 'user__email')
