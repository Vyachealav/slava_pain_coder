from core.abstract import UserModelBase


class UserModel(UserModelBase):
    def __init__(self, username: str, nickname: str, hashed_password: str, final_points: int):
        self.username = username
        self.nickname = nickname
        self.hashed_password = hashed_password
        self.final_points = final_points

    def add_points(self, points: int, *, is_correct: bool) -> None:
        """Добавляет очки пользователю"""
        self.final_points += points * int(is_correct)

    def to_dict(self) -> dict:
        """Преобразует модель пользователя в словарь"""
        return {
            'username': self.username,
            'nickname': self.nickname,
            'hashed_password': self.hashed_password,
            'final_points': self.final_points,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'UserModel':
        """Создает модель пользователя из словаря"""
        return cls(
            username=data['username'],
            nickname=data['nickname'],
            hashed_password=data['hashed_password'],
            final_points=data['final_points'],
        )
