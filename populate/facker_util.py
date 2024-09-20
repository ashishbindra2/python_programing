import re
import string

from random import shuffle
from random import randint
from random import choice
from random import choices

# from datetime import datetime
import requests
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
grating = choice(messages)
letters = string.ascii_uppercase + string.digits


def payment_detail():

    # Generate fake payment information
    payment_info = {
        "PaymentMethod": "Credit Card",
        "CreditCardType": choice(credit_card_types),  # Randomly choose a credit card type
        "CreditCardNumber": fake.credit_card_number(card_type="visa"),  # Generate a Visa card number
        "WorldpayTransactionID": fake.uuid4()  # Generate a random UUID for the transaction ID
    }
    return payment_info


def gen_company_billing():

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

    return billing_info


def item_detail(item=6):
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


data = (
    string.ascii_letters,
    string.punctuation,
    string.digits,
    string.ascii_lowercase,
    string.punctuation,
    string.ascii_uppercase,
    string.punctuation,
    string.hexdigits,
    string.ascii_letters,
)


def password_generator():
    password_list = []

    for pwd in data:
        psd = choices(pwd, k=2)
        password_list.extend(psd)

    shuffle(password_list)

    return ''.join(password_list)


# Function to download a random image from Lorem Picsum
def download_random_image(image_size=(800, 600)):
    width, height = image_size
    url = f'https://picsum.photos/{width}/{height}'

    response = requests.get(url)

    if response.status_code == 200:
        # URL might redirect to the actual image URL
        actual_url = response.url
        image_id = actual_url.split('/')[-3]
        save_image(actual_url, image_id)
    else:
        print(f"Failed to fetch image. Status code: {response.status_code}")


# Function to download image from a given URL
def save_image(url, image_id):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{image_id}.jpg', 'wb') as f:
            f.write(response.content)
        print(f"Image {image_id} downloaded successfully.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def number_generated(number=100, weight=None, k=11):
    random_numbers = list(range(0, number + 1))
    weights = [1] * (number + 1)
    if weight:
        weights[weight] = 100

    num = choices(random_numbers, weights=weights, k=k)
    return num


def faker_data(number=1):
    fk = Faker('en_IN')
    faker_list = []

    for _ in range(0, number):
        sample_data = fk.simple_profile()
        faker_list.append(sample_data)
    return faker_list


def generate_credit_card_details():

    card_info = {
        "Card Holder Name": fake.name(),
        "Card Number": fake.credit_card_number(),
        "Expiration Date": fake.credit_card_expire(),
        "Security Code (CVV)": fake.credit_card_security_code(),
        "Card Type": fake.credit_card_provider()
    }
    return card_info
