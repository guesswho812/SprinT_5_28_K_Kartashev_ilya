import pytest
from selenium import webdriver
from utils import generate_email, generate_password

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
    return "https://stellarburgers.nomoreparties.site"
