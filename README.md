# Project Three

Проект на **Django**, онлайн магазин


---

## Технологии

- Python 3.13  
- Django  
- Bootstrap  
- Postgresql

---

## Установка и запуск

1. Установить зависимости через **Poetry**:
```bash
poetry install
```

2. Команды для тестового заполнения БД:

    1. Простое добавление, добавит 3 товара в 2 категории. Команда вызывается без аргументов:
        ```bash
        python manage.py add_products
        ```
    2. Команда полностью очистит категории и продукты, *(ВНИМАНИЕ: данная команда удалит данные из БД)* Команда вызывается без аргументов:
        ```bash
        python manage.py clean_data_base
        ```
    3. Команда заполнит базу данных из json файла. Запуск команды с указанием пути к JSON-фикстуре:
        ```bash
        python manage.py add_products path/to/fixture.json
        ```

3. Запустить сервер разработки:
```bash
python manage.py runserver
```

4. Открыть в браузере локально после запуска сервера:
```bash
http://127.0.0.1:8000/
```


---

## Структура проекта

```project_three/
project_three/
├── .venv/                      # Виртуальное окружение (библиотеки)
├── catalog/                    # Приложение catalog
│   ├── management/
│   ├── migrations/
│   ├── templates/
│   │   └── catalog/
│   │       ├── includes/
│   │       │   └── inc_menu.html
│   │       ├── base.html
│   │       ├── product_detail.html
│   │       └── product_list.html
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── my_tags.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/                     # Настройки проекта (Django config)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                      # Медиафайлы
│   └── screenshots/
├── static/
│   └── catalog/
│       ├── css/
│       ├── img/
│       │   └── favicons/
│       └── js/
├── env/                        # Файлы окружения
├── env.example
├── .flake8                     # Конфигурация линтера
├── .gitignore
├── catalog_fixture.json        # Фикстуры данных
├── manage.py                   # Основной скрипт управления Django
├── poetry.lock                 # Зависимости Poetry
├── poetry.toml                 # Конфигурация Poetry
├── pyproject.toml              # Конфигурация проекта Python
├── README.md                   # Документация проекта
└── requirements.txt            # Зависимости pip```