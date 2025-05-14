from rest_framework.routers import DefaultRouter
from .views import StockViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet, basename='stocks')

urlpatterns = router.urls
