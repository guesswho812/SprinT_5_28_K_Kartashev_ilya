from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pytest

def test_successful_registration(driver):
    """Тест проверяет успешную регистрацию с валидными данными.
    
    Для регистрации используется уникальный email каждый раз,
    чтобы избежать конфликта с уже существующими пользователями.
    """
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        
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
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
        )
        register_button.click()
        
        # ПРОВЕРЯЕМ переход на логин
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url, f"Ожидался переход на логин, но URL: {driver.current_url}"
        print(f"Тест пройден: регистрация {email} успешна")
        
    except Exception as e:
        driver.save_screenshot("registration_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_registration.py::test_successful_registration -v