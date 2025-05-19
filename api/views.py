from rest_framework.views import APIView
from rest_framework.response import Response


class ApiRootView(APIView):
    def get(self, request):
        base = request.build_absolute_uri('/')[:-1]  # убираем последний слеш

        return Response({
            "home": f"{base}/api/home/",
            "stocks": f"{base}/api/stocks/",
            "watchlist": f"{base}/api/watchlist/",
            "partners": f"{base}/api/partners/",
            "auth": {
                "register": f"{base}/api/auth/register/",
                "login": f"{base}/api/auth/token/",
                "refresh": f"{base}/api/auth/token/refresh/"
            }
        })