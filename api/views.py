from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def custom_api_root(request):
    return Response({
        "partners": request.build_absolute_uri("partners/"),
        "stocks": request.build_absolute_uri("stocks/"),
        "watchlist": request.build_absolute_uri("watchlist/"),
        "home": request.build_absolute_uri("home/"),
        "auth": {
            "register": request.build_absolute_uri("auth/register/"),
            "token": request.build_absolute_uri("auth/token/"),
            "refresh": request.build_absolute_uri("auth/token/refresh/")
        },
        "referrals": request.build_absolute_uri("referrals/"),
        "subscription": request.build_absolute_uri("subscription/"),
        "profile": request.build_absolute_uri("profile/"),
    })
