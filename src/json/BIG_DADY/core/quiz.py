from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Question:
    text: str
    answer: int
    variants: list[str]
    points: int

    @classmethod
    def from_dict(cls, data: dict) -> 'Question':
        """Создает вопрос из словаря"""
        return cls(
            text=data['text'],
            answer=int(data['answer']),
            variants=data['variants'],
            points=int(data['points']),
        )


class EndOfTheGameError(Exception):
    """Исключение для обозначения конца игры"""

    pass


class Quiz:
    def __init__(self, questions: list[Question]) -> bool:
        self.questions = questions

    def is_correct_answer(self, user_answer: str) -> bool:
        """Проверка ответа пользователя"""
        if not self.questions:
            raise EndOfTheGameError('No more questions available.')
        return user_answer == self.questions.pop(0).answer
