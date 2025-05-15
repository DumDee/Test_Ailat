from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WatchedStockViewSet

router = DefaultRouter()
router.register(r'watchlist', WatchedStockViewSet, basename='watchlist')

urlpatterns = [
    path('', include(router.urls)),
]
