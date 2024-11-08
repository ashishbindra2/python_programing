import os
import io
import base64
import re
import string

import jinja2
from random import randint
from random import randint
from random import choice
from random import choices
from datetime import datetime

from jinja2 import Environment
from jinja2 import FileSystemLoader

from matplotlib import pyplot as plt
from html_to_pdf import pdf_converter
from faker import Faker

# Initialize Faker
fake = Faker()
credit_card_types = ['Visa', 'MasterCard', 'American Express', 'Discover']
# List of some currency symbols
currency_symbols = [
    '$',  # US Dollar
    '€',  # Euro
    '¥',  # Japanese Yen
    '£',  # British Pound
    'A$',  # Australian Dollar
    'C$',  # Canadian Dollar
    'CHF',  # Swiss Franc
    '₣',  # French Franc (historical)
    '₤',  # Pound Sterling (historical)
    '₽',  # Russian Ruble
    '₹',  # Indian Rupee
    '₩',  # South Korean Won
    '₪',  # Israeli New Shekel
    '฿',  # Thai Baht
    '₲',  # Paraguayan Guarani
    '₭',  # Laotian Kip
    '₨'  # Pakistani Rupee
]
# List of custom nice-day messages
messages = [
    "Wishing you a great day.",
    "Hope you have a wonderful day.",
    "Enjoy your day!",
    "Have a pleasant day.",
    "May your day be fantastic.",
    "Have a lovely day ahead.",
    "I hope your day goes well.",
    "Have an awesome day.",
    "Make it a great day.",
    "Hope your day is filled with joy."
]

letters = string.ascii_uppercase + string.digits


# invoiceNumber
# invoiceDate
# companyName
# customerName

def pay_method():
    # Define possible credit card types

    # Generate fake payment information
    payment_info = {
        "PaymentMethod": "Credit Card",
        "CreditCardType": choice(credit_card_types),  # Randomly choose a credit card type
        "CreditCardNumber": fake.credit_card_number(card_type="visa"),  # Generate a Visa card number
        "WorldpayTransactionID": fake.uuid4()  # Generate a random UUID for the transaction ID
    }

    # Generate fake billing information
    billing_info = {
        "Name": fake.name(),
        "Company": fake.company(),
        "Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state_abbr(),  # Use state abbreviation
        "ZipCode": fake.zipcode(),
        "Country": fake.country(),
        "PhoneNumber": re.sub(r'x.*', '', fake.phone_number()).strip(),
        "BillingDate": fake.date_this_year().strftime('%B %d, %Y')  # Generates a random date within the current year
    }

    return payment_info, billing_info


def populate_item_detail(item=6):
    fake_project_items = [fake.bs() for _ in range(randint(2, item))]  # 5 fake project items
    items = []
    currency = choice(currency_symbols)
    for item in fake_project_items:
        sku = "".join(choices(letters, k=7))
        qty = randint(1, 50)
        items.append({
            "itemName": item,
            "sku": sku,
            "quantity": qty,
            "currency": currency,
            "total": qty * randint(50, 800)
        })
    return items


def invoice_gen(html_name, invoice_num=5) -> None:
    """
    function to generate invoice
    :param html_name:
    :return:
    """
    file_name, _ = os.path.splitext(html_name)

    template = Environment(loader=FileSystemLoader("./templates")).get_template(html_name)

    today_date: str = datetime.now().strftime("%d-%b-%Y")
    try:
        for invoice in range(1, invoice_num):
            print(invoice)
            order = randint(1, 900000000)
            invoice_number = f"{order:0>10}"
            payment_info, billing_info = pay_method()

            context = {
                "customerName": billing_info["Name"],
                "invoiceNumber": invoice_number,
                "invoiceDate": billing_info.get("Billing Date", today_date),
                "items": populate_item_detail(),
                "billInfo": billing_info,
                "paymentMethod": payment_info,
                "Grating": choice(messages)
            }
            report_text = template.render(context)
            os.makedirs("files/invoices", exist_ok=True)

            file_path = f"./files/invoices/invoice_{file_name}_{invoice_number}"
            with open(f"{file_path}.html", mode="w", encoding="UTF-8") as f:
                f.write(report_text)

            pdf_converter(f"{file_path}.html", f"{file_path}.pdf")
    except Exception as e:
        print("Error", e)

    print("Invoice generated successfully!!!!")
