from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_go_to_profile(driver):
    """Тест проверяет переход в личный кабинет после авторизации.
    
    Шаги:
    1. Выполнить вход в систему
    2. Нажать кнопку 'Личный кабинет'
    3. Проверить переход в личный кабинет
    
    Ожидаемый результат:
    - URL содержит '/account/profile'
    """
    try:
        # Логинимся
        driver.get("https://stellarburgers.nomoreparties.site/login")
        
        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("test_killa@mail.ru")
        all_inputs[1].send_keys("qwerty123")
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()
        
        # Ожидаем завершение авторизации и переход на главную
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        # Проверяем переход в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        assert "/account/profile" in driver.current_url
        print("Тест пройден: переход в личный кабинет работает")
        
    except Exception as e:
        driver.save_screenshot("profile_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_go_to_profile.py::test_go_to_profile -v