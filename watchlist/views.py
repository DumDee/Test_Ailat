from rest_framework import viewsets, permissions, filters
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
        serializer.save(user=self.request.user)
