from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_return_to_constructor_from_profile(driver):
    """Тест проверяет переход из личного кабинета в конструктор через кнопку 'Конструктор'.
    
    Шаги:
    1. Авторизоваться и перейти в личный кабинет
    2. Нажать кнопку 'Конструктор' в шапке сайта
    3. Проверить возврат на главную страницу
    
    Ожидаемый результат:
    - URL главной страницы ('https://stellarburgers.nomoreparties.site/')
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
        
        # Возвращаемся в конструктор
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
        )
        constructor_button.click()
        
        # Проверяем возврат на главную
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("Тест пройден: переход из ЛК в конструктор через кнопку работает")
        
    except Exception as e:
        driver.save_screenshot("constructor_return_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_return_to_constructor.py::test_return_to_constructor_from_profile -v