from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

def test_burger_construction_and_order(driver):  # Используем фикстуру драйвера
    """Тест проверяет полный цикл: сборка бургера через перетаскивание и оформление заказа.
    
    Шаги:
    1. Авторизоваться в системе
    2. Перетащить ингредиент в конструктор
    3. Нажать кнопку 'Оформить заказ'
    4. Проверить появление модального окна с подтверждением заказа
    
    Ожидаемый результат:
    - Появление модального окна с текстом о начале приготовления заказа
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
        
        # Перетаскиваем ингредиент
        ingredient = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__')]"))
        )
        
        constructor_area = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]"))
        )
        
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, constructor_area).perform()
        
        # Нажимаем "Оформить заказ"
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']"))
        )
        order_button.click()
        
        # Проверяем успешное оформление заказа
        WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal__')]")),
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'орбитальной станции')]"))
            )
        )
        
        print("Тест пройден: бургер собран и заказ оформлен!")
        
    except Exception as e:
        driver.save_screenshot("error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_burger_constructor.py::test_burger_construction_and_order -v