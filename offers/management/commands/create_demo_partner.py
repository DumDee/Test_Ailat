print(">> Команда загружена")
from django.core.management.base import BaseCommand
from offers.models import Partner, Contact, ShariahBoardMember, Document, Product
from datetime import date


class Command(BaseCommand):
    help = 'Создаёт демонстрационного партнёра Amana Finance со всеми связанными моделями.'

    def handle(self, *args, **options):
        if not Partner.objects.filter(name="Amana Finance").exists():
            partner = Partner.objects.create(
                name="Amana Finance",
                description="Amana Finance — надёжная исламская финтех-компания, предлагающая продукты, соответствующие нормам шариата.",
                logo="logos/amana_logo.png",
                website="https://amana.finance",
                is_verified=True
            )

            Contact.objects.bulk_create([
                Contact(partner=partner, type='email', value='contact@amana.finance'),
                Contact(partner=partner, type='phone', value='+971 50 123 4567'),
                Contact(partner=partner, type='social', value='https://twitter.com/amanafinance')
            ])

            ShariahBoardMember.objects.bulk_create([
                ShariahBoardMember(
                    partner=partner,
                    name="Dr. Yusuf Al-Qaradawi",
                    position="Главный шариатский советник",
                    photo="shariah_photos/qaradawi.jpg"
                ),
                ShariahBoardMember(
                    partner=partner,
                    name="Sheikh Ahmad bin Saeed",
                    position="Член совета",
                    photo="shariah_photos/ahmad.jpg"
                )
            ])

            Document.objects.create(
                partner=partner,
                name="Шариатский сертификат соответствия",
                file="documents/certificate_amana.pdf",
                issue_date=date(2024, 3, 1),
                license_number="AF-SC-2024-778"
            )

            Product.objects.bulk_create([
                Product(
                    partner=partner,
                    name="Amana Wakala Investment",
                    description="Инвестиционный продукт с доверительным управлением (Wakala) и доходностью до 5.2% годовых.",
                    product_type="Wakala",
                    tags=["Investing", "Halal", "Safe"]
                ),
                Product(
                    partner=partner,
                    name="Tawarruq Personal Financing",
                    description="Финансирование на основе товарной операции (Tawarruq) — без процентов, с рассрочкой до 24 месяцев.",
                    product_type="Tawarruq",
                    tags=["Financing", "No-Riba"]
                )
            ])
            self.stdout.write(self.style.SUCCESS("Amana Finance создан"))

        # 2. Barakah Investments
        if not Partner.objects.filter(name="Barakah Investments").exists():
            partner1 = Partner.objects.create(
                name="Barakah Investments",
                description="Инвестиционная компания, работающая исключительно по шариатским принципам.",
                logo="logos/Barakah_Investments_logo.png",
                website="https://barakah.invest",
                is_verified=True
            )

            # Контакты
            Contact.objects.bulk_create([
                Contact(partner=partner1, type='email', value='info@barakah.invest'),
                Contact(partner=partner1, type='phone', value='+44 20 1234 5678'),
                Contact(partner=partner1, type='social', value='https://linkedin.com/company/barakah')
            ])

            # Шариатский совет
            ShariahBoardMember.objects.create(
                partner=partner1,
                name="Mufti Imran Khalid",
                position="Шариатский консультант",
                photo="shariah_photos/imran.png"
            )

            # Документы
            Document.objects.create(
                partner=partner1,
                name="Халал-инвестиционный сертификат",
                file="documents/barakah_cert.pdf",
                issue_date=date(2023, 11, 15),
                license_number="BK-INV-2023-112"
            )

            # Продукты
            Product.objects.bulk_create([
                Product(
                    partner=partner1,
                    name="Ethical Sukuk Portfolio",
                    description="Портфель исламских облигаций (сукук), соответствующих принципам шариата.",
                    product_type="Mudarabah",
                    tags=["Sukuk", "Portfolio"]
                ),
                Product(
                    partner=partner1,
                    name="Murabaha Trade Finance",
                    description="Финансирование торговли на основе договорённой маржи.",
                    product_type="Murabaha",
                    tags=["Trade", "Financing"]
                )
            ])
            self.stdout.write(self.style.SUCCESS("Barakah Investments создан"))

        # 3. Noor Islamic Lending
        if not Partner.objects.filter(name="Noor Islamic Lending").exists():
            partner2 = Partner.objects.create(
                name="Noor Islamic Lending",
                description="Онлайн-сервис микрофинансирования, избегающий процентов и штрафов.",
                logo="logos/noor.png",
                website="https://Noor_Islamic_Lending.org",
                is_verified=False
            )

            # Контакты
            Contact.objects.bulk_create([
                Contact(partner=partner2, type='email', value='support@noorlending.org'),
                Contact(partner=partner2, type='phone', value='+1 (800) 765-4321'),
            ])

            # Шариатский совет
            ShariahBoardMember.objects.create(
                partner=partner2,
                name="Sheikh Ali Mahmoud",
                position="Советник по шариату",
                photo="shariah_photos/ali.png"
            )

            # Документ
            Document.objects.create(
                partner=partner2,
                name="Временное разрешение шариатского комитета",
                file="documents/noor_temp_cert.pdf",
                issue_date=date(2024, 1, 10),
                license_number="NL-TEMP-2024-003"
            )

            # Продукт
            Product.objects.create(
                partner=partner2,
                name="Ijara Leasing Plan",
                description="План аренды с последующим выкупом на основе Иджара.",
                product_type="Ijara",
                tags=["Leasing", "Halal"]
            )

        self.stdout.write(self.style.SUCCESS("Noor Islamic Lending создан"))

