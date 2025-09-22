import pytest
from selenium import webdriver
from utils import generate_email, generate_password
from data import BASE_URL

@pytest.fixture
def driver():
    """Фикстура для создания и настройки драйвера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def random_email():
    return generate_email()

@pytest.fixture  
def random_password():
    return generate_password()

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def login_page(driver):
    """Фикстура для открытия страницы логина"""
    driver.delete_all_cookies()  # Очищаем куки перед открытием
    driver.get(BASE_URL + "/login")
    return driver

@pytest.fixture  
def register_page(driver):
    """Фикстура для открытия страницы регистрации"""
    driver.delete_all_cookies()  # Очищаем куки перед открытием
    driver.get(BASE_URL + "/register")
    return driver

@pytest.fixture
def forgot_password_page(driver):
    """Фикстура для открытия страницы восстановления пароля"""
    driver.delete_all_cookies()  # Очищаем куки перед открытием
    driver.get(BASE_URL + "/forgot-password")
    return driver

@pytest.fixture
def main_page(driver):
    """Фикстура для открытия главной страницы"""
    driver.delete_all_cookies()  # Очищаем куки перед открытием
    driver.get(BASE_URL + "/")
    return driver