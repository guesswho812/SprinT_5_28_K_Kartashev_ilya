from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_constructor_sections(driver):
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
    try:
        driver.get("https://stellarburgers.nomoreparties.site")
        
        # Ожидаем загрузки вкладок
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Булки']/.."))
        )
        
        # Находим все вкладки
        buns_tab = driver.find_element(By.XPATH, "//span[text()='Булки']/..")
        sauces_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']/..")
        fillings_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']/..")
        
        # Кликаем на "Соусы"
        sauces_tab.click()
        
        # Проверяем активную вкладку "Соусы"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Соусы")
        )
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Соусы" in active_tab.text
        
        # Кликаем на "Начинки"
        fillings_tab.click()
        
        # Проверяем активную вкладку "Начинки"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Начинки")
        )
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Начинки" in active_tab.text
        
        # Кликаем на "Булки"
        buns_tab.click()
        
        # Проверяем активную вкладку "Булки"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Булки")
        )
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Булки" in active_tab.text
        
        print("Тест пройден: переключение между разделами конструктора работает")
        
    except Exception as e:
        driver.save_screenshot("constructor_error.png")
        raise e

# Команда для запуска теста:
# python -m pytest tests/test_constructor.py::test_constructor_sections -v