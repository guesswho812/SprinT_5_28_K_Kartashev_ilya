import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL, REGISTER_URL, LOGIN_URL
from locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pytest

class TestRegistration:
    def test_successful_registration_format_1(self, register_page):
        """Тест проверяет успешную регистрацию с валидными данными."""
        # Страница регистрации уже открыта через фикстуру register_page
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(register_page, 10).until(
            EC.url_contains(REGISTER_URL)
        )
        
        # Генерируем уникальный email по формату из задания
        random_num = random.randint(100, 999)  # 3 цифры
        email = f"ilya_kartashev_99_{random_num}@yandex.ru"
        
        # Ожидаем появление полей ввода
        WebDriverWait(register_page, 10).until(
            EC.visibility_of_all_elements_located(RegistrationPageLocators.ALL_INPUTS)
        )
        
        # Заполняем форму корректными данными
        all_inputs = register_page.find_elements(*RegistrationPageLocators.ALL_INPUTS)
        all_inputs[0].send_keys("Илья Карташев")
        all_inputs[1].send_keys(email)
        all_inputs[2].send_keys("qwerty123")
        
        # Нажимаем кнопку регистрации
        register_button = WebDriverWait(register_page, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(register_page, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        
        assert LOGIN_URL in register_page.current_url

    def test_successful_registration_format_2(self, register_page):
        """Тест проверяет успешную регистрацию с валидными данными."""
        # Страница регистрации уже открыта через фикстуру register_page
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(register_page, 10).until(
            EC.url_contains(REGISTER_URL)
        )
        
        # Генерируем УНИКАЛЬНЫЙ email каждый раз
        random_num = random.randint(1000, 9999)
        email = f"ilya_kartashev_{random_num}@yandex.ru"
        
        # Ожидаем появление полей ввода
        WebDriverWait(register_page, 10).until(
            EC.visibility_of_all_elements_located(RegistrationPageLocators.ALL_INPUTS)
        )
        
        # Заполняем форму корректными данными
        all_inputs = register_page.find_elements(*RegistrationPageLocators.ALL_INPUTS)
        all_inputs[0].send_keys("Илья Карташев")
        all_inputs[1].send_keys(email)
        all_inputs[2].send_keys("qwerty123")
        
        # Нажимаем кнопку регистрации
        register_button = WebDriverWait(register_page, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(register_page, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        
        assert LOGIN_URL in register_page.current_url