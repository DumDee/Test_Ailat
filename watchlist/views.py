from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from .models import WatchedStock
from .serializers import WatchedStockSerializer

class WatchedStockViewSet(viewsets.ModelViewSet):
    serializer_class = WatchedStockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # фильтрация по бирже связанного Stock, поиск по имени/тикеру, сортировка по дате добавления
    filterset_fields = ['stock__exchange']
    search_fields = ['stock__name', 'stock__ticker']
    ordering_fields = ['added_at']

    def get_queryset(self):
        return WatchedStock.objects.filter(user=self.request.user).select_related('stock')

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "This stock is already in your watchlist."}
            )

    @action(detail=False, methods=['delete'], url_path='stock/(?P<stock_id>[^/.]+)')
    def destroy_by_stock(self, request, stock_id):
        instance = WatchedStock.objects.filter(user=request.user, stock_id=stock_id).first()
        if not instance:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)