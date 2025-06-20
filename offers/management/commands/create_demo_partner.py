from django.core.management.base import BaseCommand
from offers.models import Partner, Contact, ShariahBoardMember, Document, Product
from datetime import datetime

partners_data = [
    {
        "name": "Amana Finance",
        "description": "Надёжная исламская финтех-компания, предлагающая продукты, соответствующие нормам шариата.",
        "logo": "logos/amana_logo.png",
        "website": "https://amana.finance",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "contact@amana.finance"},
            {"type": "phone", "value": "+971 50 123 4567"},
            {"type": "social", "value": "https://twitter.com/amanafinance"},
        ],
        "shariah_board": [
            {"name": "Dr. Yusuf Al-Qaradawi", "position": "Главный шариатский советник", "photo": "shariah_photos/qaradawi.jpg"},
            {"name": "Sheikh Ahmad bin Saeed", "position": "Член совета", "photo": "shariah_photos/ahmad.jpg"},
        ],
        "documents": [
            {"name": "Шариатский сертификат соответствия", "file": "documents/certificate_amana.pdf", "issue_date": datetime(2024, 3, 1), "license_number": "AF-SC-2024-778"},
        ],
        "products": [
            {"name": "Amana Wakala Investment", "description": "Инвестиционный продукт с доверительным управлением (Wakala) и доходностью до 5.2% годовых.", "product_type": "Wakala", "tags": ["Investing", "Halal", "Safe"], "is_pro": False},
            {"name": "Tawarruq Personal Financing", "description": "Финансирование на основе товарной операции (Tawarruq) — без процентов, с рассрочкой до 24 месяцев.", "product_type": "Tawarruq", "tags": ["Financing", "No-Riba"], "is_pro": False},
        ],
    },
    {
        "name": "Barakah Investments",
        "description": "Инвестиционная компания, работающая исключительно по шариатским принципам.",
        "logo": "logos/Barakah_Investments_logo.png",
        "website": "https://barakah.invest",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "info@barakah.invest"},
            {"type": "phone", "value": "+44 20 1234 5678"},
            {"type": "social", "value": "https://linkedin.com/company/barakah"},
        ],
        "shariah_board": [
            {"name": "Mufti Imran Khalid", "position": "Шариатский консультант", "photo": "shariah_photos/imran.png"},
        ],
        "documents": [
            {"name": "Халал-инвестиционный сертификат", "file": "documents/barakah_cert.pdf", "issue_date": datetime(2023, 11, 15), "license_number": "BK-INV-2023-112"},
        ],
        "products": [
            {"name": "Ethical Sukuk Portfolio", "description": "Портфель исламских облигаций (сукук), соответствующих принципам шариата.", "product_type": "Mudarabah", "tags": ["Sukuk", "Portfolio"], "is_pro": False},
            {"name": "Murabaha Trade Finance", "description": "Финансирование торговли на основе договорённой маржи.", "product_type": "Murabaha", "tags": ["Trade", "Financing"], "is_pro": False},
        ],
    },
    {
        "name": "Noor Islamic Lending",
        "description": "Онлайн-сервис микрофинансирования, избегающий процентов и штрафов.",
        "logo": "logos/noor.png",
        "website": "https://Noor_Islamic_Lending.org",
        "is_verified": False,
        "contacts": [
            {"type": "email", "value": "support@noorlending.org"},
            {"type": "phone", "value": "+1 (800) 765-4321"},
        ],
        "shariah_board": [
            {"name": "Sheikh Ali Mahmoud", "position": "Советник по шариату", "photo": "shariah_photos/ali.png"},
        ],
        "documents": [
            {"name": "Временное разрешение шариатского комитета", "file": "documents/noor_temp_cert.pdf", "issue_date": datetime(2024, 1, 10), "license_number": "NL-TEMP-2024-003"},
        ],
        "products": [
            {"name": "Ijara Leasing Plan", "description": "План аренды с последующим выкупом на основе Иджара.", "product_type": "Ijara", "tags": ["Leasing", "Halal"], "is_pro": False},
        ],
    },
    {
        "name": "Sadaqah Finance",
        "description": "Финансовые услуги с акцентом на социальную ответственность и шариат.",
        "logo": "logos/sadaqah.png",
        "website": "https://sadaqah.finance",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "contact@sadaqah.finance"},
            {"type": "phone", "value": "+966 12 345 6789"},
            {"type": "social", "value": "https://facebook.com/sadaqahfinance"},
        ],
        "shariah_board": [
            {"name": "Dr. Aisha Al-Farsi", "position": "Шариатский советник", "photo": "shariah_photos/aisha.jpg"},
        ],
        "documents": [
            {"name": "Сертификат соответствия шариату", "file": "documents/sadaqah_cert.pdf", "issue_date": datetime(2023, 9, 20), "license_number": "SF-SC-2023-987"},
        ],
        "products": [
            {"name": "Halal Microfinance", "description": "Микрофинансирование с соблюдением норм шариата.", "product_type": "Mudarabah", "tags": ["Microfinance", "Halal"], "is_pro": True},
            {"name": "Zakat Investment Plan", "description": "План инвестирования с учётом обязательного закята.", "product_type": "Wakala", "tags": ["Investment", "Zakat"], "is_pro": False},
        ],
    },
    {
        "name": "Halal Wealth Management",
        "description": "Управление капиталом в соответствии с исламскими принципами.",
        "logo": "logos/halal_wealth.png",
        "website": "https://halalwealth.com",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "info@halalwealth.com"},
            {"type": "phone", "value": "+971 4 567 8901"},
        ],
        "shariah_board": [
            {"name": "Sheikh Omar Al-Khatib", "position": "Глава шариатского совета", "photo": "shariah_photos/omar.jpg"},
        ],
        "documents": [
            {"name": "Шариатское свидетельство", "file": "documents/halalwealth_cert.pdf", "issue_date": datetime(2023, 12, 5), "license_number": "HW-SC-2023-456"},
        ],
        "products": [
            {"name": "Halal Investment Fund", "description": "Фонд инвестиций с соблюдением шариата.", "product_type": "Mudarabah", "tags": ["Investment", "Halal"], "is_pro": True},
        ],
    },
    {
        "name": "Islamic Credit Union",
        "description": "Кредитный союз, предоставляющий исламские финансовые услуги.",
        "logo": "logos/islamic_credit_union.png",
        "website": "https://icu.org",
        "is_verified": False,
        "contacts": [
            {"type": "email", "value": "support@icu.org"},
            {"type": "phone", "value": "+44 1234 567890"},
        ],
        "shariah_board": [
            {"name": "Dr. Fatima Zahra", "position": "Шариатский советник", "photo": "shariah_photos/fatima.jpg"},
        ],
        "documents": [
            {"name": "Исламская финансовая лицензия", "file": "documents/icu_license.pdf", "issue_date": datetime(2024, 2, 15), "license_number": "ICU-LIC-2024-789"},
        ],
        "products": [
            {"name": "Islamic Home Financing", "description": "Ипотечное финансирование без процентов.", "product_type": "Murabaha", "tags": ["Home", "Finance"], "is_pro": False},
        ],
    },
    {
        "name": "Halal Insurance Co.",
        "description": "Компания, предоставляющая страховые продукты согласно нормам шариата.",
        "logo": "logos/halal_insurance.png",
        "website": "https://halalinsurance.com",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "contact@halalinsurance.com"},
            {"type": "phone", "value": "+966 11 234 5678"},
        ],
        "shariah_board": [
            {"name": "Sheikh Khalid Al-Mansour", "position": "Член шариатского совета", "photo": "shariah_photos/khalid.jpg"},
        ],
        "documents": [
            {"name": "Сертификат халяльного страхования", "file": "documents/halal_insurance_cert.pdf", "issue_date": datetime(2023, 8, 10), "license_number": "HIC-SC-2023-321"},
        ],
        "products": [
            {"name": "Halal Life Insurance", "description": "Страхование жизни без запрещённых элементов.", "product_type": "Tawarruq", "tags": ["Insurance", "Halal"], "is_pro": True},
        ],
    },
    {
        "name": "Islamic Investment Partners",
        "description": "Партнёры в инвестициях, соблюдающие шариатские нормы.",
        "logo": "logos/iip.png",
        "website": "https://iip.com",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "info@iip.com"},
            {"type": "phone", "value": "+971 2 345 6789"},
        ],
        "shariah_board": [
            {"name": "Dr. Ahmed Hassan", "position": "Главный шариатский советник", "photo": "shariah_photos/ahmed.jpg"},
        ],
        "documents": [
            {"name": "Инвестиционный сертификат халяль", "file": "documents/iip_cert.pdf", "issue_date": datetime(2023, 10, 20), "license_number": "IIP-SC-2023-654"},
        ],
        "products": [
            {"name": "Shariah Compliant Fund", "description": "Фонд, соответствующий нормам шариата.", "product_type": "Mudarabah", "tags": ["Investment", "Halal"], "is_pro": False},
        ],
    },
    {
        "name": "Halal Real Estate Trust",
        "description": "Траст по недвижимости, работающий по шариатским стандартам.",
        "logo": "logos/halal_real_estate.png",
        "website": "https://halalrealestate.com",
        "is_verified": False,
        "contacts": [
            {"type": "email", "value": "contact@halalrealestate.com"},
        ],
        "shariah_board": [
            {"name": "Sheikh Omar Farooq", "position": "Советник по шариату", "photo": "shariah_photos/omar_farooq.jpg"},
        ],
        "documents": [
            {"name": "Сертификат шариатского соответствия", "file": "documents/halal_real_estate_cert.pdf", "issue_date": datetime(2024, 1, 5), "license_number": "HRET-SC-2024-123"},
        ],
        "products": [
            {"name": "Ijara Property Lease", "description": "Договор аренды недвижимости по Иджара.", "product_type": "Ijara", "tags": ["Leasing", "Halal"], "is_pro": True},
        ],
    },
    {
        "name": "Tawhid Capital",
        "description": "Капитал с фокусом на исламские инвестиции.",
        "logo": "logos/tawhid_capital.png",
        "website": "https://tawhidcapital.com",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "info@tawhidcapital.com"},
            {"type": "phone", "value": "+44 207 123 4567"},
        ],
        "shariah_board": [
            {"name": "Dr. Sami Al-Majid", "position": "Глава шариатского совета", "photo": "shariah_photos/sami.jpg"},
        ],
        "documents": [
            {"name": "Шариатское свидетельство", "file": "documents/tawhid_capital_cert.pdf", "issue_date": datetime(2023, 7, 25), "license_number": "TC-SC-2023-987"},
        ],
        "products": [
            {"name": "Halal Growth Fund", "description": "Фонд роста с соблюдением шариата.", "product_type": "Mudarabah", "tags": ["Investment", "Halal"], "is_pro": False},
        ],
    },
    {
        "name": "Zakat Solutions",
        "description": "Решения для управления закятом и благотворительностью.",
        "logo": "logos/zakat_solutions.png",
        "website": "https://zakatsolutions.org",
        "is_verified": False,
        "contacts": [
            {"type": "email", "value": "support@zakatsolutions.org"},
        ],
        "shariah_board": [
            {"name": "Sheikh Bilal Hassan", "position": "Советник по закяту", "photo": "shariah_photos/bilal.jpg"},
        ],
        "documents": [
            {"name": "Сертификат соответствия закяту", "file": "documents/zakat_cert.pdf", "issue_date": datetime(2023, 11, 30), "license_number": "ZS-SC-2023-456"},
        ],
        "products": [
            {"name": "Zakat Management Platform", "description": "Платформа для эффективного управления закятом.", "product_type": "Other", "tags": ["Charity", "Zakat"], "is_pro": False},
        ],
    },
    {
        "name": "Halal Food Network",
        "description": "Сеть поставщиков халяль продуктов питания.",
        "logo": "logos/halal_food.png",
        "website": "https://halalfoodnetwork.com",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "contact@halalfoodnetwork.com"},
            {"type": "phone", "value": "+971 6 123 4567"},
        ],
        "shariah_board": [
            {"name": "Dr. Nadia Rahman", "position": "Шариатский контролёр", "photo": "shariah_photos/nadia.jpg"},
        ],
        "documents": [
            {"name": "Сертификат халяль качества", "file": "documents/halal_food_cert.pdf", "issue_date": datetime(2024, 2, 12), "license_number": "HFN-SC-2024-789"},
        ],
        "products": [
            {"name": "Halal Food Certification", "description": "Сертификация продуктов питания по стандартам халяль.", "product_type": "Other", "tags": ["Certification", "Halal"], "is_pro": True},
        ],
    },
    {
        "name": "Islamic Microfinance Fund",
        "description": "Фонд микрофинансирования для поддержки малого бизнеса по шариатским нормам.",
        "logo": "logos/islamic_microfinance.png",
        "website": "https://islamicmicrofinance.org",
        "is_verified": True,
        "contacts": [
            {"type": "email", "value": "info@islamicmicrofinance.org"},
        ],
        "shariah_board": [
            {"name": "Sheikh Abdullah Karim", "position": "Советник по микрофинансированию", "photo": "shariah_photos/abdullah.jpg"},
        ],
        "documents": [
            {"name": "Микрофинансовая лицензия", "file": "documents/microfinance_license.pdf", "issue_date": datetime(2023, 10, 5), "license_number": "IMF-LIC-2023-321"},
        ],
        "products": [
            {"name": "Microfinance Loan Program", "description": "Программа займов для малого бизнеса без процентов.", "product_type": "Mudarabah", "tags": ["Microfinance", "Halal"], "is_pro": False},
        ],
    },
]


class Command(BaseCommand):
    help = 'Создаёт демонстрационных партнёров с контактами, советом, документами и продуктами.'

    def handle(self, *args, **options):
        for p_data in partners_data:
            partner, created = Partner.objects.get_or_create(
                name=p_data["name"],
                defaults={
                    "description": p_data["description"],
                    "logo": p_data["logo"],
                    "website": p_data["website"],
                    "is_verified": p_data["is_verified"],
                }
            )

            Contact.objects.bulk_create([
                Contact(partner=partner, **contact)
                for contact in p_data.get("contacts", [])
            ])

            ShariahBoardMember.objects.bulk_create([
                ShariahBoardMember(partner=partner, **member)
                for member in p_data.get("shariah_board", [])
            ])

            Document.objects.bulk_create([
                Document(partner=partner, **doc)
                for doc in p_data.get("documents", [])
            ])

            Product.objects.bulk_create([
                Product(partner=partner, **product)
                for product in p_data.get("products", [])
            ])

        self.stdout.write(self.style.SUCCESS("Партнёры созданы успешно"))
