from rest_framework import serializers
from .models import (
    Partner, Contact, ShariahBoardMember, Document,
    Product, IssueReport
)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class ShariahBoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShariahBoardMember
        fields = ['id', 'name', 'photo', 'position']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'name', 'file', 'issue_date', 'license_number']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'product_type', 'tags', 'partner']


class IssueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueReport
        fields = ['id', 'product', 'description', 'created_at']


class PartnerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    shariah_board = ShariahBoardMemberSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'description', 'logo', 'website', 'is_verified',
            'contacts', 'shariah_board', 'documents', 'products'
        ]