from rest_framework import viewsets
from .models import Partner, Contact, ShariahBoardMember, Document, Product, IssueReport
from .serializers import (
    PartnerSerializer, ContactSerializer, ShariahBoardMemberSerializer,
    DocumentSerializer, ProductSerializer, IssueReportSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # фильтрация по типу продукта, pro-статусу и тегам; поиск по названию/описанию
    filterset_fields = ['product_type', 'is_pro', 'tags__name']
    search_fields = ['name', 'description']
    ordering_fields = ['yield_rate', 'name']

class IssueReportViewSet(viewsets.ModelViewSet):
    queryset = IssueReport.objects.all()
    serializer_class = IssueReportSerializer


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer