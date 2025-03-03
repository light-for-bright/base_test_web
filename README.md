# Web Testing Framework

Фреймворк для автоматического тестирования веб-сайтов с использованием Selenium и Python.

## Структура проекта

```
website_testing/
├── config/         # Конфигурационные файлы
├── pages/          # Page Objects
├── tests/          # Тестовые файлы
├── reports/        # Отчеты о тестировании
├── utils/          # Вспомогательные утилиты
└── requirements.txt # Зависимости проекта
```

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Конфигурация

1. Создайте файл `.env` в корневой директории проекта:
```
BROWSER=chrome
HEADLESS=False
BASE_URL=https://example.com
USERNAME=test_user
PASSWORD=test_password
```

## Запуск тестов

Запуск всех тестов:
```bash
pytest
```

Запуск конкретного теста:
```bash
pytest tests/test_login.py
```

Запуск тестов с генерацией Allure-отчета:
```bash
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
```

## Создание новых тестов

1. Создайте новый Page Object в директории `pages/`
2. Создайте новый тестовый файл в директории `tests/`
3. Используйте существующие фикстуры из `conftest.py`

## Особенности

- Автоматическое создание скриншотов при падении тестов
- Поддержка Allure-отчетов
- Page Object паттерн
- Поддержка Chrome и Firefox
- Конфигурация через переменные окружения
- Гибкая структура проекта

## Требования

- Python 3.7+
- Chrome или Firefox браузер
- Соответствующий WebDriver (устанавливается автоматически) 