import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import TEST_EMAIL, TEST_PASSWORD, BASE_URL, LOGIN_URL, MAIN_URL
from locators import MainPageLocators, LoginPageLocators, CommonLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class TestBurgerConstructor:
    def test_burger_construction_and_order(self, login_page):
        """Тест проверяет полный цикл: сборка бургера через перетаскивание и оформление заказа."""
        # Страница логина уже открыта через фикстуру login_page
        
        # Увеличиваем время ожидания и добавляем проверку URL
        WebDriverWait(login_page, 15).until(
            EC.url_contains(LOGIN_URL)
        )
        
        # Ожидаем появление полей ввода (увеличиваем время)
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
        
        # Перетаскиваем ингредиент
        ingredient = WebDriverWait(login_page, 15).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT)
        )
        
        constructor_area = WebDriverWait(login_page, 15).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
        )
        
        actions = ActionChains(login_page)
        actions.drag_and_drop(ingredient, constructor_area).perform()
        
        # Нажимаем "Оформить заказ"
        order_button = WebDriverWait(login_page, 15).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        order_button.click()
        
        # Проверяем успешное оформление заказа
        WebDriverWait(login_page, 15).until(
            EC.any_of(
                EC.visibility_of_element_located(CommonLocators.MODAL_WINDOW),
                EC.visibility_of_element_located(CommonLocators.ORDER_SUCCESS_TEXT)
            )
        )
        
        # Проверяем что модальное окно отображается
        modal = WebDriverWait(login_page, 15).until(
            EC.visibility_of_element_located(CommonLocators.MODAL_WINDOW)
        )
        assert modal.is_displayed(), "Модальное окно заказа не отобразилось"

    def test_switch_to_sauces_tab(self, main_page):
        """Тест проверяет переключение на вкладку 'Соусы'."""
        # Главная страница уже открыта через фикстуру main_page
        
        # Ожидаем загрузки вкладок
        WebDriverWait(main_page, 15).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        
        # Находим вкладки
        sauces_tab = main_page.find_element(*MainPageLocators.SAUCES_TAB)
        
        # Скроллим к элементу и ждем кликабельности
        main_page.execute_script("arguments[0].scrollIntoView();", sauces_tab)
        
        WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        )
        
        # Кликаем на "Соусы" через JavaScript
        main_page.execute_script("arguments[0].click();", sauces_tab)
        
        # Проверяем активную вкладку "Соусы"
        WebDriverWait(main_page, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.CURRENT_TAB, "Соусы")
        )
        active_tab = main_page.find_element(*MainPageLocators.CURRENT_TAB)
        assert "Соусы" in active_tab.text, "Вкладка 'Соусы' не активировалась"

    def test_switch_to_fillings_tab(self, main_page):
        """Тест проверяет переключение на вкладку 'Начинки'."""
        # Главная страница уже открыта через фикстуру main_page
        
        # Ожидаем загрузки вкладок
        WebDriverWait(main_page, 15).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        
        # Находим вкладки
        fillings_tab = main_page.find_element(*MainPageLocators.FILLINGS_TAB)
        
        # Скроллим к элементу и ждем кликабельности
        main_page.execute_script("arguments[0].scrollIntoView();", fillings_tab)
        
        WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        )
        
        # Кликаем на "Начинки" через JavaScript
        main_page.execute_script("arguments[0].click();", fillings_tab)
        
        # Проверяем активную вкладку "Начинки"
        WebDriverWait(main_page, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.CURRENT_TAB, "Начинки")
        )
        active_tab = main_page.find_element(*MainPageLocators.CURRENT_TAB)
        assert "Начинки" in active_tab.text, "Вкладка 'Начинки' не активировалась"

    def test_switch_to_buns_tab(self, main_page):
        """Тест проверяет переключение на вкладку 'Булки'."""
        # Главная страница уже открыта через фикстуру main_page
        
        # Ожидаем загрузки вкладок
        WebDriverWait(main_page, 15).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        
        # Находим вкладки
        buns_tab = main_page.find_element(*MainPageLocators.BUNS_TAB)
        
        # Скроллим к элементу и ждем кликабельности
        main_page.execute_script("arguments[0].scrollIntoView();", buns_tab)
        
        WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        )
        
        # Кликаем на "Булки" через JavaScript
        main_page.execute_script("arguments[0].click();", buns_tab)
        
        # Проверяем активную вкладку "Булки"
        WebDriverWait(main_page, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.CURRENT_TAB, "Булки")
        )
        active_tab = main_page.find_element(*MainPageLocators.CURRENT_TAB)
        assert "Булки" in active_tab.text, "Вкладка 'Булки' не активировалась"