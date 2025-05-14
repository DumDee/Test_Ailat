from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PartnerViewSet, ProductViewSet, IssueReportViewSet, DocumentViewSet
)

router = DefaultRouter()
router.register(r'partners', PartnerViewSet, basename='partners')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'issues', IssueReportViewSet, basename='issues')
router.register(r'documents', DocumentViewSet, basename='documents')

urlpatterns = [
    path('', include(router.urls)),
]
