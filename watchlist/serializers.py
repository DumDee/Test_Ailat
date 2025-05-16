from rest_framework import serializers
from .models import WatchedStock
from stocks.models import Stock
from stocks.serializers import StockSerializer  # если хочешь вложенные данные об акции


class WatchedStockSerializer(serializers.ModelSerializer):
    stock = serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all())
    stock_detail = StockSerializer(source='stock', read_only=True)

    class Meta:
        model = WatchedStock
        fields = ['id', 'stock', 'stock_detail', 'notifications_enabled', 'added_at']
