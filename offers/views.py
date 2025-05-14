from rest_framework import viewsets
from .models import Partner, Contact, ShariahBoardMember, Document, Product, IssueReport
from .serializers import (
    PartnerSerializer, ContactSerializer, ShariahBoardMemberSerializer,
    DocumentSerializer, ProductSerializer, IssueReportSerializer
)


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class IssueReportViewSet(viewsets.ModelViewSet):
    queryset = IssueReport.objects.all()
    serializer_class = IssueReportSerializer


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer