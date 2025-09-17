from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_via_register_form(driver):
    """Тест проверяет переход на страницу логина со страницы регистрации.
    
    Шаги:
    1. Открыть страницу регистрации
    2. Нажать ссылку 'Войти' под формой
    3. Проверить переход на страницу логина
    
    Ожидаемый результат:
    - URL содержит '/login'
    """
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register")
        )
        
        # Нажимаем ссылку "Войти"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        )
        login_link.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url
        print("Тест пройден: переход на логин со страницы регистрации работает")
        
    except Exception as e:
        driver.save_screenshot("register_form_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_login_via_register_form.py::test_login_via_register_form -v