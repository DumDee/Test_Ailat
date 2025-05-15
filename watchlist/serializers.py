from rest_framework import serializers
from .models import WatchedStock
from stocks.serializers import StockSerializer  # если хочешь вложенные данные об акции


class WatchedStockSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)

    class Meta:
        model = WatchedStock
        fields = ['id', 'stock', 'notifications_enabled', 'added_at']
