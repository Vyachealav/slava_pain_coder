import json
from core.abstract import QuizDBBase
from core.quiz import Question, Quiz


class JsonQuizDB(QuizDBBase):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.questions = self.load_questions()

    def load_questions(self) -> Quiz:
        """Загружает вопросы из JSON файла"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                questions_data = json.load(file)
                questions = [Question.from_dict(q) for q in questions_data]
                return Quiz(questions)
        except FileNotFoundError:
            return []
