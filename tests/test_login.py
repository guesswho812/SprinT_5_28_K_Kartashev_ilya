import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestLogin:
    def test_login_via_personal_account(self, driver):
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
        driver.get(BASE_URL)
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        # Нажимаем кнопку "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
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
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Проверяем успешный вход и переход на главную
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_register_form(self, driver):
        """Тест проверяет переход на страницу логина со страницы регистрации.
        
        Шаги:
        1. Открыть страницу регистрации
        2. Нажать ссылку 'Войти' под формой
        3. Проверить переход на страницу логина
        
        Ожидаемый результат:
        - URL содержит '/login'
        """
        driver.get(BASE_URL + "/register")
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register")
        )
        
        # Нажимаем ссылку "Войти"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url

    def test_login_via_forgot_password(self, driver):
        """Тест проверяет переход на страницу логина со страницы восстановления пароля.
        
        Шаги:
        1. Открыть страницу восстановления пароля
        2. Нажать ссылку 'Войти' под формой
        3. Проверить переход на страницу логина
        
        Ожидаемый результат:
        - URL содержит '/login'
        """
        driver.get(BASE_URL + "/forgot-password")
        
        # Ожидаем загрузки страницы восстановления пароля
        WebDriverWait(driver, 10).until(
            EC.url_contains("/forgot-password")
        )
        
        # Нажимаем ссылку "Войти"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url

    def test_login_from_main_page(self, driver):
        """Тест проверяет вход через кнопку 'Войти в аккаунт' на главной странице.
        
        Шаги:
        1. Открыть главную страницу
        2. Нажать кнопку 'Войти в аккаунт'
        3. Проверить переход на страницу логина
        
        Ожидаемый результат: 
        - URL содержит '/login'
        """
        driver.get(BASE_URL)
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        # Нажимаем кнопку "Войти в аккаунт"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)
        )
        login_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url

# Команды для запуска тестов:
# python -m pytest tests/test_login.py::TestLogin::test_login_via_personal_account -v
# python -m pytest tests/test_login.py::TestLogin::test_login_via_register_form -v
# python -m pytest tests/test_login.py::TestLogin::test_login_via_forgot_password -v
# python -m pytest tests/test_login.py::TestLogin::test_login_from_main_page -v
# python -m pytest tests/test_login.py -v  # запуск всех тестов класса