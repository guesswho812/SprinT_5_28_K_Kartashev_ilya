import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL, TEST_EMAIL, TEST_PASSWORD, LOGIN_URL, PROFILE_URL, MAIN_URL
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestNavigation:
    def test_go_to_profile(self, login_page):
        """Тест проверяет переход в личный кабинет после авторизации."""
        # Страница логина уже открыта через фикстуру login_page (куки уже очищены)
        
        print("Открыта страница логина, текущий URL:", login_page.current_url)
        
        # Сначала убедимся что мы на правильной странице
        WebDriverWait(login_page, 15).until(
            EC.url_contains(LOGIN_URL)
        )
        print("Подтвержден переход на страницу логина")
        
        # Ожидаем появление полей ввода
        WebDriverWait(login_page, 15).until(
            EC.visibility_of_all_elements_located(LoginPageLocators.ALL_INPUTS)
        )
        print("Поля ввода найдены")
        
        all_inputs = login_page.find_elements(*LoginPageLocators.ALL_INPUTS)
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        print("Данные для ввода заполнены")
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        print("Кнопка входа нажата")
        
        # Ожидаем завершение авторизации
        WebDriverWait(login_page, 15).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        print("Авторизация успешна, перешли на главную")
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()
        print("Кнопка личного кабинета нажата")
        
        # Проверяем переход в личный кабинет
        WebDriverWait(login_page, 15).until(
            EC.url_contains(PROFILE_URL)
        )
        print("Успешный переход в личный кабинет")
        
        assert PROFILE_URL in login_page.current_url

    def test_logout_from_profile(self, login_page):
        """Тест проверяет выход из аккаунта через кнопку 'Выйти'."""
        # Страница логина уже открыта через фикстуру login_page (куки уже очищены)
        
        # Ожидаем появление полей ввода
        WebDriverWait(login_page, 15).until(
            EC.visibility_of_all_elements_located(LoginPageLocators.ALL_INPUTS)
        )
        
        all_inputs = login_page.find_elements(*LoginPageLocators.ALL_INPUTS)
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Ожидаем завершение авторизации
        WebDriverWait(login_page, 15).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()
        
        # Ожидаем загрузки личного кабинета
        WebDriverWait(login_page, 15).until(
            EC.url_contains(PROFILE_URL)
        )
        
        # Нажимаем кнопку "Выйти"
        logout_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        # Проверяем выход (переход на логин)
        WebDriverWait(login_page, 15).until(
            EC.url_contains(LOGIN_URL)
        )
        
        assert LOGIN_URL in login_page.current_url

    def test_return_to_constructor_from_profile(self, login_page):
        """Тест проверяет переход из ЛК в конструктор через кнопку 'Конструктор'."""
        # Страница логина уже открыта через фикстуру login_page (куки уже очищены)
        
        # Ожидаем появление полей ввода
        WebDriverWait(login_page, 15).until(
            EC.visibility_of_all_elements_located(LoginPageLocators.ALL_INPUTS)
        )
        
        all_inputs = login_page.find_elements(*LoginPageLocators.ALL_INPUTS)
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Ожидаем завершение авторизации
        WebDriverWait(login_page, 15).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()
        
        # Ожидаем загрузки личного кабинета
        WebDriverWait(login_page, 15).until(
            EC.url_contains(PROFILE_URL)
        )
        
        # Возвращаемся в конструктор
        constructor_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()
        
        # Проверяем возврат на главную
        WebDriverWait(login_page, 15).until(
            EC.url_to_be(BASE_URL + MAIN_URL)
        )
        
        assert login_page.current_url == BASE_URL + MAIN_URL