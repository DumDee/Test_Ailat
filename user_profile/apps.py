from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
    verbose_name = ('Профили пользователей')

    def ready(self):
        import user_profile.signals