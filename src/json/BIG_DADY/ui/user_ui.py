from typing import final
from user.abstract import UserUIBase
from user.forms import LoginForm, RegistrationForm


@final
class ConsoleUserUI(UserUIBase):
    def get_user_input(self) -> str:
        """Получает ввод пользователя из консоли"""
        return input('Введите данные: ')

    def registration_form(self) -> RegistrationForm:
        """Отображает форму регистрации пользователя и считывает данные"""
        username = input('Введите имя пользователя: ')
        nickname = input('Введите никнейм: ')
        password = input('Введите пароль: ')
        return RegistrationForm(username=username, nickname=nickname, password=password)

    def login_form(self) -> LoginForm:
        """Отображает форму входа пользователя и считывает данные"""
        username = input('Введите имя пользователя для входа: ')
        password = input('Введите пароль: ')
        return LoginForm(username=username, password=password)


console_user_ui = ConsoleUserUI()
