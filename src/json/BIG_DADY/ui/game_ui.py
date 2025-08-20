from typing import final
from core.abstract import GameUIBase


@final
class ConsoleGameUI(GameUIBase):
    def display_question(self, question: str, variants: list[str]) -> None:
        print(f'Вопрос: {question}')
        for index, variant in enumerate(variants):
            print(f'{index + 1}. {variant}')

    def get_user_answer(self) -> int:
        answer = input('Введите номер вашего ответа: ')
        return int(answer)

    def display_result(self, is_correct: bool, points: int) -> None:
        if is_correct:
            print(f'Верно! Вы заработали {points} очков.')
        else:
            print('Неверно. Попробуйте следующий вопрос.')

    def display_final_score(self, score: int) -> None:
        print(f'Игра окончена! Ваш итоговый счет: {score} очков.')


console_game_ui = ConsoleGameUI()
