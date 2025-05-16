from rest_framework import viewsets, permissions, filters, serializers
from django.db import IntegrityError
from .models import WatchedStock
from .serializers import WatchedStockSerializer

class WatchedStockViewSet(viewsets.ModelViewSet):
    serializer_class = WatchedStockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['stock__name', 'stock__ticker']

    def get_queryset(self):
        return WatchedStock.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "This stock is already in your watchlist."}
            )
