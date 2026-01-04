from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
            "avatar",
            "phone",
            "country",
        )
        labels = {
            "email": "Email",
            "avatar": "Аватар",
            "phone": "Номер телефона",
            "country": "Страна",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Подтверждение пароля"

        self.fields["password1"].help_text = "Минимум 8 символов, не простой пароль."
        self.fields["password2"].help_text = "Введите тот же пароль ещё раз."
        self.fields["phone"].help_text = (
            "Введите номер телефона в международном формате."
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите email",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Повторите пароль",
            }
        )

        self.fields["phone"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "+7XXXXXXXXXX",
            }
        )

        self.fields["country"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["avatar"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
