from abc import ABC, abstractmethod

from core.quiz import Quiz


class UserModelBase(ABC):
    def __init__(self, final_points: str) -> None:
        self.final_points = final_points

    @abstractmethod
    def add_points(self, points: int, *, is_correct: bool) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Преобразует модель пользователя в словарь"""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> 'UserModelBase':
        """Создает модель пользователя из словаря"""
        pass


class GameUIBase(ABC):
    @abstractmethod
    def display_question(self, question: str, variants: list[str]) -> None:
        """Отображает вопрос и варианты ответов"""
        pass

    @abstractmethod
    def get_user_answer(self) -> int:
        """Получает ответ пользователя"""
        pass

    @abstractmethod
    def display_result(self, is_correct: bool, points: int) -> None:
        """Отображает результат ответа пользователя"""
        pass

    @abstractmethod
    def display_final_score(self, score: int) -> None:
        """Отображает итоговый счет пользователя"""
        pass


class QuizDBBase(ABC):
    @abstractmethod
    def load_questions(self) -> Quiz:
        """Получает список вопросов из базы данных"""
        pass
