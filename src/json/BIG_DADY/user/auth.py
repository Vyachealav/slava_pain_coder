import hashlib
from user.abstract import UserDBBase, UserUIBase
from user.user import UserModel


def hash_password(password: str) -> str:
    """Хешируем с солью пароль для безопасности"""
    pwd_salt = password + 'good_salt'
    return hashlib.sha256(pwd_salt.encode()).hexdigest()


class UnknownUserError(Exception):
    """Ошибка, возникающая при попытке авторизации неизвестного пользователя."""

    pass


class Registration:
    def __init__(self, ui: UserUIBase, db: UserDBBase) -> None:
        self.ui = ui
        self.user_db = db

    def register(self) -> UserModel:
        """Регистрирует пользователя и возвращает модель пользователя"""
        registration_form = self.ui.registration_form()
        user_model = UserModel(
            registration_form.username,
            registration_form.nickname,
            hash_password(registration_form.password),
            final_points=0,
        )
        self.user_db.save_user(user_model)
        return user_model


class Authorization:
    def __init__(self, ui: UserUIBase, db: UserDBBase) -> None:
        self.ui = ui
        self.db = db

    def login(self) -> UserModel:
        """Авторизует пользователя и возвращает модель пользователя"""
        login_form = self.ui.login_form()
        username = login_form.username
        password = login_form.password
        hashed_password = hash_password(password)
        user = self.db.get_user_by_username(username)
        if user and user.hashed_password == hashed_password:
            return user
        raise UnknownUserError(f'Пользователь с именем {username} не найден или пароль неверен')
