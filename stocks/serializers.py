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

class StockDetailSerializer(serializers.ModelSerializer):
    is_compliant = serializers.SerializerMethodField()
    icon_url = serializers.SerializerMethodField()
    screening = serializers.SerializerMethodField()
    status_history = ComplianceStatusHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = [
            'id', 'name', 'ticker', 'exchange', 'country', 'sector', 'industry',
            'current_price', 'change_value', 'change_percent', 'currency',
            'compliance_status', 'is_compliant', 'icon_url', 'last_updated',
            'status_history', 'screening'
        ]

    def get_is_compliant(self, obj):
        return obj.compliance_status == 'compliant'

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.icon_url:
            return request.build_absolute_uri(obj.icon_url)
        return None

    def get_screening(self, obj):
        screening = ShariahScreening.objects.filter(stock=obj).order_by('-screening_date').first()
        if screening:
            return ShariahScreeningSerializer(screening).data
        return None