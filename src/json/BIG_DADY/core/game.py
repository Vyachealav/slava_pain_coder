from core.abstract import GameUIBase, UserModelBase
from core.quiz import EndOfTheGameError, Quiz


class Game:
    def __init__(self, quiz: Quiz, user: UserModelBase, ui: GameUIBase) -> None:
        self.quiz = quiz
        self.user = user
        self.ui = ui

    def start(self) -> None:
        while True:
            try:
                question = self.quiz.questions[0]
                self.ui.display_question(question.text, question.variants)
                user_answer_index = self.ui.get_user_answer()
                is_correct = self.quiz.is_correct_answer(user_answer_index)
                self.user.add_points(question.points, is_correct=is_correct)
                self.ui.display_result(is_correct, question.points)
            except (EndOfTheGameError, IndexError):
                self.ui.display_final_score(self.user.final_points)
                break
