import pytest
from selenium import webdriver
from utils import generate_email, generate_password
from data import BASE_URL  # Импортируем напрямую BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
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
    return BASE_URL  # Используем импортированную константу