from rest_framework import generics, permissions
from .models import Referral
from .serializers import ReferralSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralListView(generics.ListAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Referral.objects.filter(referrer=self.request.user).select_related('referrer', 'referred')

