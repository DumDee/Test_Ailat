from django.urls import path
from .views import ProfileView, PinCreateView, PinVerifyView, delete_profile

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('pin/create/', PinCreateView.as_view(), name='pin_create'),
    path('pin/verify/', PinVerifyView.as_view(), name='pin_verify'),
    path("profile/delete/", delete_profile)
]
