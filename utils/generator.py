import random
import random
from faker import Faker
import uuid

fake = Faker('id_ID')

def random_item():
    brands = ["Pajero", "Fortuner", "Civic", "CRV", "Innova", "Avanza", "Xpander", "Destinator", "X-Force"]
    types = ["Sport", "Dakar", "Turbo", "Hybrid", "4x4", "Ultimate", "EV", "Pro", "Pro Max", "Plus", "Lite"]
    return f"{random.choice(brands)} {random.choice(types)}"


def random_company():
    return fake.company()


def random_npwp():
    return str(random.randint(10**15, 10**16 - 1))


def random_email():
    return fake.email()


def random_phone():
    return fake.phone_number()


def random_payment_days():
    return str(random.randint(0, 360))


def random_address():
    return fake.address()


def random_city():
    return fake.city()


def random_country():
    return fake.country_code()


def random_postal_code():
    return fake.postcode()


def random_note():
    return fake.text(max_nb_chars=200)


def random_name(num_words=1):
    return fake.sentence(nb_words=num_words)


def random_coa():
    brands = ["Cash", "Bank", "Accounts", "Owner", "Sales"]
    types = ["BCA", "BNI", "BRI", "Mandiri", "Permata", "Receivable", "Payable", "Capital", "Revenue", "Expense"]
    return f"{random.choice(brands)} {random.choice(types)}"


def random_type_coa():
    type = ["Asset", "Liability", "Equity", "Revenue", "Expense"]
    return f"{random.choice(type)}"


def random_price_list():
    category = ["Retail", "Wholesale", "Wholesale", "Export", "Export", "Promo", "VIP"]
    subcategory = ["Price", "Standard", "Customer Price"]
    return f"{random.choice(category)} {random.choice(subcategory)}"


def random_uom():
    uom = ["KG", "Meter", "Roll", "Unit", "Kodi", "GigaByte", "Centimeter", "PCS", "Pack"]
    return f"{random.choice(uom)}"


def random_currency():
    return fake.currency_code()


def random_currency_symbol():
    symbols = [
        "$", "€", "£", "¥", "₩", "₽", "₹", "₫", "฿", "₴", "₦",
        "₱", "₲", "₵", "₸", "₺", "₼", "₾", "₡",
        "₠", "₢", "₣", "₤", "₥", "₧", "₰",
        "Rp", "R$", "CHF", "kr", "zł"]

    return f"{random.choice(symbols)}"
