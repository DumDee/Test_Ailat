from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"

    def __str__(self):
        return self.name


class Contact(models.Model):
    CONTACT_TYPES = (
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('social', 'Social Media'),
    )
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='contacts')
    type = models.CharField(max_length=50, choices=CONTACT_TYPES)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.type}: {self.value}"


class ShariahBoardMember(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='shariah_board')
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='shariah_photos/', blank=True, null=True)
    position = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Член шариатского совета"
        verbose_name_plural = "Члены шариатского совета"

    def __str__(self):
        return self.name


class Document(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    issue_date = models.DateField()
    license_number = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPES = (
        ('Wakala', 'Wakala'),           # Доверительное инвестирование
        ('Tawarruq', 'Tawarruq'),       # Получение ликвидности через товар
        ('Murabaha', 'Murabaha'),       # Продажа с наценкой (часто для финансирования)
        ('Mudarabah', 'Mudarabah'),     # Партнёрство: один даёт деньги, другой работает
        ('Ijara', 'Ijara'),             # Лизинг или аренда
        ('Istisna', 'Istisna'),         # Производство под заказ (например, недвижимость)
        ('Salam', 'Salam'),             # Предоплата за товар, который будет поставлен позже
    )

    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    product_type = models.CharField(max_length=100, choices=PRODUCT_TYPES)
    tags = models.JSONField(default=list, blank=True)
    is_pro = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class IssueReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='issues')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"

    def __str__(self):
        return f"Issue for {self.product.name}"
