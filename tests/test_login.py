from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_from_main_page(driver):
    """Тест проверяет вход через кнопку 'Войти в аккаунт' на главной странице.
    
    Шаги:
    1. Открыть главную страницу
    2. Нажать кнопку 'Войти в аккаунт'
    3. Проверить переход на страницу логина
    
    Ожидаемый результат: 
    - URL содержит '/login'
    """
    try:
        driver.get("https://stellarburgers.nomoreparties.site")
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        
        # Нажимаем кнопку "Войти в аккаунт"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url
        print("Тест пройден: переход на страницу логина работает")
        
    except Exception as e:
        driver.save_screenshot("main_page_login_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_login.py::test_login_from_main_page -v