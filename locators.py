# Файл: locators.py
# Описание всех локаторов для проекта Stellar Burgers
from selenium.webdriver.common.by import By

class LoginPageLocators:
    \"\"\"Локаторы для страницы логина\"\"\"
    
    # Поля ввода
    EMAIL_INPUT = (By.XPATH, \"//input[@type='text']\")  # Поле email
    PASSWORD_INPUT = (By.XPATH, \"//input[@type='password']\")  # Поле пароля
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, \"//button[text()='Войти']\")  # Кнопка \"Войти\"
    REGISTER_LINK = (By.XPATH, \"//a[text()='Зарегистрироваться']\")  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.XPATH, \"//a[text()='Восстановить пароль']\")  # Восстановление пароля

class MainPageLocators:
    \"\"\"Локаторы для главной страницы\"\"\"
    
    # Кнопки авторизации
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, \"//button[text()='Войти в аккаунт']\")  # Кнопка входа
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, \"//p[text()='Личный Кабинет']\")  # Личный кабинет
    
    # Конструктор бургеров
    CONSTRUCTOR_BUTTON = (By.XPATH, \"//p[text()='Конструктор']\")  # Кнопка конструктора
    BUNS_TAB = (By.XPATH, \"//span[text()='Булки']/..\")  # Вкладка \"Булки\"
    SAUCES_TAB = (By.XPATH, \"//span[text()='Соусы']/..\")  # Вкладка \"Соусы\"
    FILLINGS_TAB = (By.XPATH, \"//span[text()='Начинки']/..\")  # Вкладка \"Начинки\"
    
    # Ингредиенты
    INGREDIENT = (By.XPATH, \"//div[contains(@class, 'BurgerIngredient_ingredient__')]\")  # Любой ингредиент
    CONSTRUCTOR_AREA = (By.XPATH, \"//div[contains(@class, 'BurgerConstructor_basket__')]\")  # Область конструктора
    
    # Оформление заказа
    ORDER_BUTTON = (By.XPATH, \"//button[text()='Оформить заказ']\")  # Кнопка оформления заказа

class RegistrationPageLocators:
    \"\"\"Локаторы для страницы регистрации\"\"\"
    
    NAME_INPUT = (By.XPATH, \"(//input)[1]\")  # Поле имени
    EMAIL_INPUT = (By.XPATH, \"(//input)[2]\")  # Поле email
    PASSWORD_INPUT = (By.XPATH, \"(//input)[3]\")  # Поле пароля
    REGISTER_BUTTON = (By.XPATH, \"//button[text()='Зарегистрироваться']\")  # Кнопка регистрации
    LOGIN_LINK = (By.XPATH, \"//a[text()='Войти']\")  # Ссылка на вход

class ForgotPasswordPageLocators:
    \"\"\"Локаторы для страницы восстановления пароля\"\"\"
    
    LOGIN_LINK = (By.XPATH, \"//a[text()='Войти']\")  # Ссылка на вход

class ProfilePageLocators:
    \"\"\"Локаторы для личного кабинета\"\"\"
    
    LOGOUT_BUTTON = (By.XPATH, \"//button[text()='Выход']\")  # Кнопка выхода

class CommonLocators:
    \"\"\"Общие локаторы для всех страниц\"\"\"
    
    MODAL = (By.XPATH, \"//div[contains(@class, 'Modal_modal__')]\")  # Модальное окно
    ORDER_SUCCESS_TEXT = (By.XPATH, \"//*[contains(text(), 'орбитальной станции')]\")  # Текст успешного заказа
