from rest_framework.views import APIView
from rest_framework.response import Response
from stocks.models import Stock
from offers.models import Partner

class HomeAPIView(APIView):

    def get(self, request):
        # Подсчёт compliant / non-compliant акций
        compliant_count = Stock.objects.filter(compliance_status='compliant').count()
        non_compliant_count = Stock.objects.filter(compliance_status='non_compliant').count()

        # Примеры акций (можно заменить на .filter или .order_by)
        example_stocks = Stock.objects.all()[:3]

        # Примеры партнёров
        top_partners = Partner.objects.all()[:5]

        # Статичные продукты Ailat
        products = [
            {"title": "Stock screening", "description": "...", "icon": "stock"},
            {"title": "Market Offers", "description": "...", "icon": "offer"},
            {"title": "Education Center", "description": "...", "icon": "edu"},
            {"title": "Zakat Calculation", "description": "...", "icon": "zakat"},
        ]

        return Response({
            "sharia_screening": {
                "compliant_count": compliant_count,
                "non_compliant_count": non_compliant_count,
                "example_stocks": [
                    {
                        "name": stock.name,
                        "ticker": stock.ticker,
                        "is_compliant": stock.compliance_status == 'compliant'
                    }
                    for stock in example_stocks
                ]
            },
            "stock_investments": [
                {
                    "name": stock.name,
                    "price": stock.current_price,
                    "ticker": stock.ticker,
                    "change_value": stock.change_value,
                    "change_percent": stock.change_percent,
                    "currency": stock.currency,
                    "icon_url": stock.icon_url
                }
                for stock in example_stocks
            ],
            "products": products,
            "market_offers": [
                {
                    "bank": partner.name,
                    "description": partner.description,
                    "logo_url": request.build_absolute_uri(partner.logo.url) if partner.logo else None,
                    "website": partner.website
                }
                for partner in top_partners
            ]
        })