from django.contrib import admin
from .models import (
    Stock,
    ShariahScreening,
    ComplianceCriteria,
    ComplianceStatusHistory,
)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'ticker',
        'name',
        'exchange',
        'country',
        'current_price',
        'change_value',
        'change_percent',
        'compliance_status',
        'last_updated',
    )
    list_filter = ('exchange', 'country', 'compliance_status', 'currency', 'sector')
    search_fields = ('ticker', 'name', 'industry', 'sector')
    ordering = ('-last_updated',)


class ComplianceCriteriaInline(admin.TabularInline):
    model = ComplianceCriteria
    extra = 0


@admin.register(ShariahScreening)
class ShariahScreeningAdmin(admin.ModelAdmin):
    list_display = ('stock', 'screening_date', 'result_status', 'source')
    list_filter = ('result_status',)
    search_fields = ('stock__ticker', 'stock__name', 'source')
    inlines = [ComplianceCriteriaInline]


@admin.register(ComplianceCriteria)
class ComplianceCriteriaAdmin(admin.ModelAdmin):
    list_display = ('screening', 'category', 'percentage', 'status')
    list_filter = ('category', 'status')
    search_fields = ('screening__stock__ticker',)


@admin.register(ComplianceStatusHistory)
class ComplianceStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('stock', 'status', 'date')
    list_filter = ('status',)
    search_fields = ('stock__ticker', 'stock__name')
