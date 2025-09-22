# Sprint 5 - UI Автотесты для Stellar Burgers

## Описание проекта
Автоматизированные UI-тесты для космического фастфуда "Stellar Burgers".

## Функциональность покрытая тестами
- Регистрация
- Авторизация  
- Личный кабинет
- Конструктор бургеров
- Оформление заказа
- Выход из системы

## Технологический стек
- Python 3.13
- Selenium WebDriver  
- Pytest
- Page Object Pattern

## Структура проекта
Sprint_5/
├── tests/                          # Директория с тестами
│   ├── test_registration.py        # Тесты регистрации
│   ├── test_login.py               # Тесты авторизации
│   ├── test_burger_constructor.py  # Тесты конструктора
│   ├── test_go_to_profile.py       # Тесты личного кабинета
│   ├── test_logout.py              # Тесты выхода из системы
│   └── conftest.py                 # Фикстуры Pytest
├── pages/                          # Page Object Model
├── utils.py                        # Генераторы тестовых данных
├── requirements.txt                # Зависимости проекта
└── README.md                       # Документация

## Установка и запуск
1. Активировать виртуальное окружение: venv\Scripts\activate
2. Установить зависимости: pip install -r requirements.txt
3. Запустить тесты: pytest tests/ -v

## Автор
Илья Карташев - студент 28-ой когорты QA Automation Engineer

## Лицензия
Учебный проект Яндекс Практикум
