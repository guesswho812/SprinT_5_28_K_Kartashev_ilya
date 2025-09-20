import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL
from locators import RegistrationPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pytest

class TestRegistration:
    def test_successful_registration_format_1(self, driver):
        """Тест проверяет успешную регистрацию с валидными данными.
        
        Для регистрации используется уникальный email по формату: 
        имя_фамилия_номеркогорты_3цифры@домен (требование задания)
        Это гарантирует, что каждый запуск теста создает нового пользователя.
        """
        driver.get(BASE_URL + "/register")
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register")
        )
        
        # Генерируем уникальный email по формату из задания
        random_num = random.randint(100, 999)  # 3 цифры
        email = f"ilya_kartashev_99_{random_num}@yandex.ru"
        
        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        # Заполняем форму корректными данными
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("Илья Карташев")
        all_inputs[1].send_keys(email)  # Уникальный email
        all_inputs[2].send_keys("qwerty123")  # Пароль >6 символов
        
        # Нажимаем кнопку регистрации
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()
        
        # Проверяем переход на страницу логина после успешной регистрации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url, f"Ожидался переход на логин, но URL: {driver.current_url}"

    def test_successful_registration_format_2(self, driver):
        """Тест проверяет успешную регистрацию с валидными данными.
        
        Для регистрации используется уникальный email каждый раз,
        чтобы избежать конфликта с уже существующими пользователями.
        """
        driver.get(BASE_URL + "/register")
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register")
        )
        
        # Генерируем УНИКАЛЬНЫЙ email каждый раз
        random_num = random.randint(1000, 9999)  # Увеличиваем диапазон
        email = f"ilya_kartashev_{random_num}@yandex.ru"  # Меняем шаблон
        
        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        # Заполняем форму корректными данными
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("Илья Карташев")
        all_inputs[1].send_keys(email)  # Используем уникальный email!
        all_inputs[2].send_keys("qwerty123")
        
        # Нажимаем кнопку регистрации
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()
        
        # ПРОВЕРЯЕМ переход на логин
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url, f"Ожидался переход на логин, но URL: {driver.current_url}"

# Команды для запуска тестов:
# python -m pytest tests/test_registration.py::TestRegistration::test_successful_registration_format_1 -v
# python -m pytest tests/test_registration.py::TestRegistration::test_successful_registration_format_2 -v
# python -m pytest tests/test_registration.py -v  # запуск всех тестов класса
