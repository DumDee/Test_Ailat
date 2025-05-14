from django.contrib import admin
from .models import (
    Partner, Contact, ShariahBoardMember,
    Document, Product, IssueReport
)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_verified', 'website')
    search_fields = ('name',)
    list_filter = ('is_verified',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('partner', 'type', 'value')
    list_filter = ('type',)


@admin.register(ShariahBoardMember)
class ShariahBoardMemberAdmin(admin.ModelAdmin):
    list_display = ('partner', 'name', 'position')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('partner', 'name', 'license_number', 'issue_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner', 'product_type')
    list_filter = ('product_type',)
    search_fields = ('name',)


@admin.register(IssueReport)
class IssueReportAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'created_at')
    search_fields = ('description',)
