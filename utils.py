import random
import string

def generate_email():
    """Генератор email адресов"""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yandex.ru', 'mail.ru', 'yahoo.com'])
    return f"{username}@{domain}"

def generate_password(length=10):
    """Генератор паролей"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def generate_name(length=6):
    """Генератор имен"""
    return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()
