from rest_framework import serializers
from .models import Stock, ShariahScreening, ComplianceCriteria, ComplianceStatusHistory


class ComplianceCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceCriteria
        fields = ['id', 'category', 'percentage', 'status']


class ShariahScreeningSerializer(serializers.ModelSerializer):
    criteria = ComplianceCriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = ShariahScreening
        fields = ['id', 'screening_date', 'result_status', 'comment', 'source', 'criteria']


class ComplianceStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceStatusHistory
        fields = ['id', 'status', 'date']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'ticker', 'exchange', 'country', 'current_price', 'change_value', 'change_percent',
            'currency',
            'sector', 'industry',
            'compliance_status', 'icon_url',
            'trading_view_ticker', 'tinkoff_link',
            'last_updated',
        ]
