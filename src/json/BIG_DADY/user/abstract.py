from abc import ABC, abstractmethod

from user.forms import LoginForm, RegistrationForm
from user.user import UserModel


class UserUIBase(ABC):
    @abstractmethod
    def get_user_input(self) -> str:
        """Получает ввод пользователя"""
        pass

    @abstractmethod
    def registration_form(self) -> RegistrationForm:
        """Отображает форму регистрации пользователя и считывает данные"""
        pass

    @abstractmethod
    def login_form(self) -> LoginForm:
        """Отображает форму входа пользователя и считывает данные"""
        pass


class UserDBBase(ABC):
    @abstractmethod
    def save_user(self, user: UserModel) -> None:
        """Сохраняет модель пользователя в базе данных"""
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserModel:
        """Получает модель пользователя из базы данных по имени пользователя"""
        pass
