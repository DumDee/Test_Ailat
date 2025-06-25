from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer, StockDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["ticker", "exchange"]
    search_fields = ["name", "ticker"]
    ordering_fields = ["current_price", "ticker"]

    def get_queryset(self):
        user = self.request.user
        qs = Stock.objects.all()

        qs = qs.prefetch_related(
            'screenings__criteria',
            'status_history'
        )

        if not (
            user.is_authenticated and
            hasattr(user, 'subscription') and
            user.subscription.is_active and
            user.subscription.type  in ['pro', 'plus']
        ):
            qs = qs.filter(is_free_access=True)

        return qs

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StockDetailSerializer
        return StockSerializer
