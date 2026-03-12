from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Регистрируем нашу кастомную модель User в админке
@admin.register(User)
class UserAdmin(UserAdmin):
    # ⬆️ КЛЮЧЕВОЙ МОМЕНТ
    # Мы наследуемся НЕ от admin.ModelAdmin,
    # а от django.contrib.auth.admin.UserAdmin.
    #
    # Если бы здесь был ModelAdmin:
    #  ❌ пароль сохранялся бы как обычный текст
    #  ❌ не было бы кнопки "Сменить пароль"
    #  ❌ логин не работал бы

    # ---------
    # НАСТРОЙКИ СПИСКА ПОЛЬЗОВАТЕЛЕЙ
    # ---------

    # Поля, которые отображаются в списке пользователей
    # Оставляем твои поля без изменений
    list_display = (
        "id",
        "email",
        "country",
    )

    # Фильтры справа в админке
    list_filter = ("country",)

    # Поля, по которым работает поиск
    search_fields = ("email",)

    # Сортировка пользователей (по email)
    ordering = ("email",)

    # ---------
    # ФОРМА РЕДАКТИРОВАНИЯ ПОЛЬЗОВАТЕЛЯ
    # ---------

    fieldsets = (
        # Основная информация
        # password — НЕ обычное поле,
        # Django сам заменит его на:
        # "Raw passwords are not stored..."
        (None, {"fields": ("email", "password")}),

        # Дополнительные поля пользователя
        ("Дополнительно", {
            "fields": ("country",)
        }),

        # Права и группы
        ("Права доступа", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
    )

    # ---------
    # ФОРМА СОЗДАНИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ
    # ---------

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),

                # 🔑 САМОЕ ВАЖНОЕ МЕСТО
                #
                # password1 и password2:
                #  ✔ проверяются на совпадение
                #  ✔ проходят валидаторы пароля
                #  ✔ АВТОМАТИЧЕСКИ ХЕШИРУЮТСЯ
                #
                # Если здесь был бы просто "password":
                #  ❌ пароль сохранился бы как обычный текст
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
