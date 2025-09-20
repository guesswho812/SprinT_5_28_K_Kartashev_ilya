import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestNavigation:
    def test_go_to_profile(self, driver):
        """Тест проверяет переход в личный кабинет после авторизации."""
        # Логинимся
        driver.get(BASE_URL + "/login")
        
        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Ожидаем завершение авторизации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()
        
        # Проверяем переход в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        assert "/account/profile" in driver.current_url

    def test_logout_from_profile(self, driver):
        """Тест проверяет выход из аккаунта через кнопку 'Выйти'."""
        # Логинимся
        driver.get(BASE_URL + "/login")
        
        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Ожидаем завершение авторизации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()
        
        # Ожидаем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        # Нажимаем кнопку "Выйти"
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        # Проверяем выход (переход на логин)
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url

    def test_return_to_constructor_from_profile(self, driver):
        """Тест проверяет переход из ЛК в конструктор через кнопку 'Конструктор'."""
        # Логинимся
        driver.get(BASE_URL + "/login")
        
        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
        )
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys(TEST_EMAIL)
        all_inputs[1].send_keys(TEST_PASSWORD)
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Ожидаем завершение авторизации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        # Переходим в личный кабинет
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()
        
        # Ожидаем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        # Возвращаемся в конструктор
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()
        
        # Проверяем возврат на главную
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )
        
        assert driver.current_url == BASE_URL + "/"