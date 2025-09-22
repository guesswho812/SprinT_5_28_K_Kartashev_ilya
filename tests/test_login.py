import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL, TEST_EMAIL, TEST_PASSWORD, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL, MAIN_URL
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestLogin:
    def test_login_via_personal_account(self, main_page):
        """Тест проверяет вход через кнопку 'Личный кабинет' без авторизации."""
        # Главная страница уже открыта через фикстуру main_page
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(main_page, 10).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        
        # Нажимаем кнопку "Личный кабинет"
        personal_account_button = WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(main_page, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        assert LOGIN_URL in main_page.current_url
        
        # Выполняем вход
        WebDriverWait(main_page, 10).until(
            EC.visibility_of_all_elements_located(LoginPageLocators.ALL_INPUTS)
        )
        
        all_inputs = main_page.find_elements(*LoginPageLocators.ALL_INPUTS)
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        login_button = WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Проверяем успешный вход и переход на главную
        WebDriverWait(main_page, 10).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        
        assert main_page.current_url == BASE_URL + MAIN_URL

    def test_login_via_register_form(self, register_page):
        """Тест проверяет переход на страницу логина со страницы регистрации."""
        # Страница регистрации уже открыта через фикстуру register_page
        
        # Ожидаем загрузки страницы регистрации
        WebDriverWait(register_page, 10).until(
            EC.url_contains(REGISTER_URL)
        )
        
        # Нажимаем ссылку "Войти"
        login_link = WebDriverWait(register_page, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(register_page, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        
        assert LOGIN_URL in register_page.current_url

    def test_login_via_forgot_password(self, forgot_password_page):
        """Тест проверяет переход на страницу логина со страницы восстановления пароля."""
        # Страница восстановления пароля уже открыта через фикстуру forgot_password_page
        
        # Ожидаем загрузки страницы восстановления пароля
        WebDriverWait(forgot_password_page, 10).until(
            EC.url_contains(FORGOT_PASSWORD_URL)
        )
        
        # Нажимаем ссылку "Войти"
        login_link = WebDriverWait(forgot_password_page, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(forgot_password_page, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        
        assert LOGIN_URL in forgot_password_page.current_url

    def test_login_from_main_page(self, main_page):
        """Тест проверяет вход через кнопку 'Войти в аккаунт' на главной странице."""
        # Главная страница уже открыта через фикстуру main_page
        
        # Ожидаем загрузки главной страницы
        WebDriverWait(main_page, 10).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        
        # Нажимаем кнопку "Войти в аккаунт"
        login_button = WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)
        )
        login_button.click()
        
        # Проверяем переход на страницу логина
        WebDriverWait(main_page, 10).until(
            EC.url_contains(LOGIN_URL)
        )
        
        assert LOGIN_URL in main_page.current_url