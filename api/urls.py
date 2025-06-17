from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import custom_api_root

# импорт router’ов из apps
from offers.urls import router as offers_router
from stocks.urls import router as stocks_router
from watchlist.urls import router as watchlist_router

# собираем все router'ы
router = SimpleRouter()
router.registry.extend(offers_router.registry)
router.registry.extend(stocks_router.registry)
router.registry.extend(watchlist_router.registry)

urlpatterns = [
    path('', custom_api_root, name='api-root'),
    *router.urls,

    path('auth/', include('auth_api.urls')),
    path('home/', include('home.urls')),
    path('referrals/', include('referrals.urls')),
    path('subscription/', include('subscriptions.urls')),
    path('profile/', include('user_profile.urls')),

]
