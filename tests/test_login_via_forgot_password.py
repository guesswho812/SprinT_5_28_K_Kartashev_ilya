from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_via_forgot_password(driver):
    """Тест проверяет переход на страницу логина со страницы восстановления пароля.
    
    Шаги:
    1. Открыть страницу восстановления пароля
    2. Нажать ссылку 'Войти' под формой
    3. Проверить переход на страницу логина
    
    Ожидаемый результат:
    - URL содержит '/login'
    """
    try:
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        
        # Ожидаем загрузки страницы восстановления пароля
        WebDriverWait(driver, 10).until(
            EC.url_contains("/forgot-password")
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
        print("Тест пройден: переход на логин со страницы восстановления пароля работает")
        
    except Exception as e:
        driver.save_screenshot("forgot_password_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_login_via_forgot_password.py::test_login_via_forgot_password -v