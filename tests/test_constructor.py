import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import TEST_EMAIL, TEST_PASSWORD, BASE_URL
from locators import MainPageLocators, LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class TestBurgerConstructor:
    def test_burger_construction_and_order(self, driver):
        """Тест проверяет полный цикл: сборка бургера через перетаскивание и оформление заказа.
        
        Шаги:
        1. Авторизоваться в системе
        2. Перетащить ингредиент в конструктор
        3. Нажать кнопку 'Оформить заказ'
        4. Проверить появление модального окна с подтверждением заказа
        
        Ожидаемый результат:
        - Появление модального окна с текстом о начале приготовления заказа
        """
        # Логинимся
        driver.get(f"{BASE_URL}/login")
        
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
        
        # Перетаскиваем ингредиент
        ingredient = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT)
        )
        
        constructor_area = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
        )
        
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, constructor_area).perform()
        
        # Нажимаем "Оформить заказ"
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        order_button.click()
        
        # Проверяем успешное оформление заказа
        WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal__')]")),
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'орбитальной станции')]"))
            )
        )
        
        # Проверяем что модальное окно отображается
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal__')]"))
        )
        assert modal.is_displayed(), "Модальное окно заказа не отобразилось"

    def test_constructor_sections(self, driver):
        """Тест проверяет переключение между разделами конструктора: 'Булки', 'Соусы', 'Начинки'.
        
        Шаги:
        1. Открыть главную страницу
        2. Найти вкладки разделов
        3. Последовательно кликнуть на каждую вкладку
        4. Проверить активацию соответствующей вкладки
        
        Ожидаемый результат:
        - При клике на вкладку она становится активной
        - Отображается соответствующий раздел с ингредиентами
        """
        driver.get(BASE_URL)
        
        # Ожидаем загрузки вкладок
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        
        # Находим все вкладки
        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)
        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)
        fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        
        # Кликаем на "Соусы"
        sauces_tab.click()
        
        # Проверяем активную вкладку "Соусы"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Соусы")
        )
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Соусы" in active_tab.text, "Вкладка 'Соусы' не активировалась"
        
        # Кликаем на "Начинки"
        fillings_tab.click()
        
        # Проверяем активную вкладку "Начинки"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Начинки")
        )
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Начинки" in active_tab.text, "Вкладка 'Начинки' не активировалась"
        
        # Кликаем на "Булки"
        buns_tab.click()
        
        # Проверяем активную вкладку "Булки"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Булки")
        )
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Булки" in active_tab.text, "Вкладка 'Булки' не активировалась"

# Команды для запуска тестов:
# python -m pytest tests/test_burger_constructor.py::TestBurgerConstructor::test_burger_construction_and_order -v
# python -m pytest tests/test_burger_constructor.py::TestBurgerConstructor::test_constructor_sections -v
# python -m pytest tests/test_burger_constructor.py -v  # запуск всех тестов класса