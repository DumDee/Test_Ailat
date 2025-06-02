from django.urls import path
from .views import ReferralListView

urlpatterns = [
    path('my-referrals/', ReferralListView.as_view(), name='my-referrals'),
]
