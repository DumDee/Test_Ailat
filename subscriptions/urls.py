from django.urls import path
from .views import UserSubscriptionView, ActivateSubscriptionView

urlpatterns = [
    path('', UserSubscriptionView.as_view(), name='user_subscription'),
    path('activate/', ActivateSubscriptionView.as_view(), name='activate_subscription'),
]
