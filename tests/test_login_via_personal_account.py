from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_via_personal_account(driver):
    """Тест проверяет вход через кнопку 'Личный кабинет' без авторизации.
    
    Шаги:
    1. Открыть главную страницу
    2. Нажать кнопку 'Личный кабинет'
    3. Проверить переход на страницу логина
    4. Выполнить вход с валидными данными
    5. Проверить переход на главную страницу
    
    Ожидаемый результат:
    - Успешный вход и переход на главную страницу
    """
    try:
        driver.get("https://stellarburgers.nomoreparties.site")
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        
        # Нажимаем кнопку "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        personal_account_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
        
        # Выполняем вход
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("test_killa@mail.ru")
        all_inputs[1].send_keys("qwerty123")
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()
        
        # Проверяем успешный вход и переход на главную
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("Тест пройден: вход через личный кабинет работает")
        
    except Exception as e:
        driver.save_screenshot("personal_account_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_login_via_personal_account.py::test_login_via_personal_account -v