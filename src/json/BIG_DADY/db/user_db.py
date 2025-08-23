import json
from typing import final

from user.abstract import UserDBBase
from user.user import UserModel


@final
class JsonUserDB(UserDBBase):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self) -> dict[str, UserModel]:
        """Загружает пользователей из JSON файла"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return {x['username']: UserModel.from_dict(x) for x in json.load(file)}
        except FileNotFoundError:
            return {}

    def save_user(self, user: UserModel) -> None:
        """Сохраняет модель пользователя в базе данных"""
        self.users[user.username] = user
        self.save_users()

    def save_users(self) -> None:
        """Сохраняет всех пользователей в JSON файл"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([user.to_dict() for _, user in self.users.items()], file, indent=4)

    def get_user_by_username(self, username: str) -> UserModel:
        """Получает модель пользователя из базы данных по имени пользователя"""
        user_data = self.users.get(username)
        if user_data:
            return UserModel(
                username=user_data.username,
                nickname=user_data.nickname,
                hashed_password=user_data.hashed_password,
                final_points=user_data.final_points,
            )
        return None
