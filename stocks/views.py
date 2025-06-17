from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer, StockDetailSerializer


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        user = self.request.user
        qs = Stock.objects.all()

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
