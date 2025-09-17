from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_logout_from_profile(driver):
    """Тест проверяет выход из аккаунта через кнопку 'Выйти' в личном кабинете.
    
    Шаги:
    1. Авторизоваться и перейти в личный кабинет
    2. Нажать кнопку 'Выйти'
    3. Проверить переход на страницу логина
    
    Ожидаемый результат:
    - URL содержит '/login'
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
        
        # Ожидаем завершение авторизации
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        # Ожидаем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        # Нажимаем кнопку "Выйти"
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
        )
        logout_button.click()
        
        # Проверяем выход (переход на логин)
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url
        print("Тест пройден: выход из аккаунта работает корректно")
        
    except Exception as e:
        driver.save_screenshot("logout_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_logout.py::test_logout_from_profile -v