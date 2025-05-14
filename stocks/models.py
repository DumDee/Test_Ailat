from django.db import models

# Акции
class Stock(models.Model):
    COMPLIANCE_CHOICES = [
        ('compliant', 'Compliant'),
        ('non_compliant', 'Non-compliant'),
        ('doubtful', 'Doubtful'),
        ('forbidden', 'Forbidden'),  # из JSON был такой статус
    ]

    name = models.CharField(max_length=255)  # shortName
    ticker = models.CharField(max_length=10, unique=True)
    exchange = models.CharField(max_length=50)  # NASDAQ, NYSE, MOEX
    country = models.CharField(max_length=100)

    current_price = models.DecimalField(max_digits=12, decimal_places=2)
    change_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # dailyChange
    change_percent = models.DecimalField(max_digits=6, decimal_places=2, default=0)  # dailyChangePercents
    currency = models.CharField(max_length=10)  # usd, rub и т.д.

    sector = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=150, blank=True, null=True)

    compliance_status = models.CharField(
        max_length=20,
        choices=COMPLIANCE_CHOICES,
        default='doubtful'
    )

    icon_url = models.URLField(blank=True, null=True)  # /logo/...
    trading_view_ticker = models.CharField(max_length=50, blank=True, null=True)
    tinkoff_link = models.URLField(blank=True, null=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ticker} ({self.name})"

# Шариатская проверка
class ShariahScreening(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='screenings')
    screening_date = models.DateField()
    result_status = models.CharField(max_length=20, choices=Stock.COMPLIANCE_CHOICES)
    comment = models.TextField(blank=True)
    source = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Screening for {self.stock.ticker} — {self.screening_date}"

# Критерий соответствия
class ComplianceCriteria(models.Model):
    CRITERIA_CHOICES = [
        ('income', 'Income'),
        ('debt', 'Debt'),
        ('deposits', 'Deposits'),
        ('halal', 'Halal Activities'),
        ('other', 'Other'),
    ]

    screening = models.ForeignKey(ShariahScreening, on_delete=models.CASCADE, related_name='criteria')
    category = models.CharField(max_length=50, choices=CRITERIA_CHOICES)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=Stock.COMPLIANCE_CHOICES)

    def __str__(self):
        return f"{self.category} — {self.percentage}%"

# История статусов
class ComplianceStatusHistory(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='status_history')
    status = models.CharField(max_length=20, choices=Stock.COMPLIANCE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.stock.ticker} — {self.status} on {self.date}"