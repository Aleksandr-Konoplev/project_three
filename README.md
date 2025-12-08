# Project Three

Проект на **Django**, который на данный момент выводит две страницы: 

- **Главная** (`home`)  
- **Контакты** (`contacts`)

---

## Технологии

- Python 3.13  
- Django  
- Bootstrap  
- SQLite  

---

## Установка и запуск

1. Установить зависимости через **Poetry**:
```bash
poetry install
```

2. Запустить сервер разработки:
```bash
python manage.py runserver
```

3. Открыть в браузере:
```bash
http://127.0.0.1:8000/
```

4. Команда для тестового заполнения БД (ВНИМАНИЕ: Данная команда удалит данные из БД):
```bash
python manage.py add_products
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
│   │       ├── base_html
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
│       │   └── bootstrap.min.css
│       ├── img/
│       │   └── favicons/
│       │       ├── android-chrome-192x192.png
│       │       ├── android-chrome-512x512.png
│       │       ├── apple-touch-icon.png
│       │       ├── favicon.ico
│       │       ├── favicon-16x16.png
│       │       ├── favicon-32x32.png
│       │       ├── safari-pinned-tab.svg
│       │       └── manifest.json
│       └── js/
│           ├── bootstrap.bundle.min.js
│           └── color-modes.js
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