# Project Three

Проект на **Django**, онлайн магазин и блог с отзывами


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
   
    4. Команда заполнит базу данных из json файла, для приложения "Блог"
        ```bash
        python manage.py loaddata blog/fixtures/posts.json
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
│
├── .venv/                    # Виртуальное окружение (корень библиотек)
├── .env                      # Переменные окружения
├── .env.example              # Пример переменных окружения
├── .flake8                   # Конфигурация линтера
├── .gitignore                # Игнорируемые файлы Git
├── manage.py                 # Точка входа Django
├── pyproject.toml           # Конфигурация Poetry
├── poetry.lock              # Зависимости Poetry
├── poetry.toml              # Конфигурация Poetry
├── requirements.txt         # Зависимости проекта (альтернатива Poetry)
├── README.md                # Описание проекта
├── catalog_fixture.json     # Фикстуры для каталога
│
├── config/                  # Основной конфигурационный модуль Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── catalog/                 # Приложение "catalog"
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       ├── add_products.py
│   │       ├── add_products_from_fixture.py
│   │       └── clean_data_base.py
│   │
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_category_description_alter_category_name_and_more.py
│   │   └── __init__.py
│   │
│   ├── templatetags/       # Пользовательские теги шаблонов
│   │   ├── __init__.py
│   │   └── my_tags.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── blog/                    # Приложение "blog"
│   ├── fixtures/
│   │   └── posts.json      # Фикстуры для постов блога
│   │
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   │
│   ├── templatetags/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/               # Общие шаблоны проекта
│   ├── includes/
│   │   ├── inc_menu.html
│   │   └── ...
│   ├── base.html
│   ├── contacts.html
│   ├── product_detail.html
│   ├── product_list.html
│   │
│   ├── blog/               # Шаблоны приложения blog
│   │   ├── includes/
│   │   │   └── inc_menu.html
│   │   ├── base.html
│   │   ├── delete_post.html
│   │   ├── post_detail.html
│   │   ├── post_form.html
│   │   └── posts_list.html
│   │
│   └── catalog/            # Шаблоны приложения catalog
│       └── includes/
│           └── ...
│
├── media/                   # Медиафайлы (загружаемые пользователями)
│   ├── img_of_blog_post/
│   ├── products/
│   └── screenshots/
│
└── static/                  # Статические файлы
    ├── blog/
    │   └── css/
    │       └── bootstrap.min.css
    │
    ├── catalog/
    │   ├── css/
    │   │   └── bootstrap.min.css
    │   ├── img/
    │   │   └── favicons/
    │   │       ├── android-chrome-192x192.png
    │   │       ├── android-chrome-512x512.png
    │   │       ├── apple-touch-icon.png
    │   │       ├── favicon.ico
    │   │       ├── favicon-16x16.png
    │   │       ├── favicon-32x32.png
    │   │       ├── manifest.json
    │   │       └── safari-pinned-tab.svg
    │   └── js/
    │       ├── bootstrap.bundle.min.js
    │       └── color-modes.js
    │
    ├── img/
    │   ├── favicons/       (дубликат или альтернативное расположение)
    │   │   ├── android-chrome-192x192.png
    │   │   ├── android-chrome-512x512.png
    │   │   └── ...
    │   └── logo/
    │       ├── shopaholics_logo_dark.png
    │       └── shopaholics_logo_light.png
    │
    └── js/
        ├── bootstrap.bundle.min.js
        └── color-modes.js
```