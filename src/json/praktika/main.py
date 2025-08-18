# 15 points
# Доработать программу квиза. Такой функционал нужно добавить(#прогердобавь):

# 1. Добавить возможность добавлять пользователей
#     1. Какие данные нужны — имя, ник, общий счёт (сколько за всё время набрал баллов),
#     персональный сгенинрированный сложный пароль для пользователя
#     2. Сохранять информацию о пользователе в json
#     3. Функционал авторизации
#         1. Обновление общего счёта после каждой игры
# 3. Свой модуль название_модуля_для_работы_с_json

# Посмотрите внимательно на функции, связанные с работой с файлами json. Не кажется, что мы копипастим код?
# Да и функционал в целом можно вынести в отдельные функции. Это всё смахивает на написание своего модуля.


import os
import inspect
import json
import secrets
import actions_with_json
import typing

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = f'{DIR}/data/data.json'
JSON_USERS_PATH = f'{DIR}/data/users.json'


class Question:
    def __init__(self, question_hash: dict[str, typing.Any]) -> None:
        self.text: str = question_hash['text']
        self.answer: str = question_hash['answer']
        self.variants: list[str] = question_hash['variants']
        self.points: int = int(question_hash['points'])
        self.question_hash = question_hash

    def __str__(self) -> str:
        result = f"""
                  Вопрос: {self.text}
                  Баллы за правильный овтет: {self.points}
                  """
        return inspect.cleandoc(result)

    @staticmethod
    def questions() -> list['Question']:
        """Получаем все вопросы из json файла"""

        data = actions_with_json.read_json_data_file()

        questions = []
        for question_hash in data:
            new_question = Question(question_hash)
            questions.append(new_question)

        return questions

    def append_to_json(self) -> None:
        data = actions_with_json.read_json_data_file()

        data.append(self.question_hash)

        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)


class Quiz:
    def __init__(self, questions: list['Question']) -> None:
        self.questions = questions
        self.total_points = 0

    def is_true_answer(self, question: 'Question', user_answer_index: int) -> bool:
        return user_answer_index == question.variants.index(question.answer)

    def add_points(self, question: 'Question') -> None:
        self.total_points += question.points


class Authorization:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def is_authorization(self) -> bool:
        users = actions_with_json.read_json_users_file()
        return any(self.username == user.get('username') and self.password == user.get('password') for user in users)

    def add_points_total(self, question: 'Question') -> None:
        users = actions_with_json.read_json_users_file()

        for user in users:
            if user['username'] == self.username:
                user['points'] += question.points
                break
        with open(JSON_USERS_PATH, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False)


def registration(username: str, nickname: str) -> None:
    password = secrets.token_hex(16)
    final_points = 0
    user_data = {
        'username': username,
        'nickname': nickname,
        'password': password,
        'points': final_points,
    }
    data = actions_with_json.read_json_users_file()

    data.append(user_data)

    with open(JSON_USERS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    print(f'Вы успешно зарегистрировались, ваш пароль: {password}')


def show_menu() -> None:
    print("""
Добро пожаловать в викторину!
1. Зарегистрироваться
2. Авторизоваться
0. Выход
""")


def main() -> None:
    while True:
        show_menu()
        choice = input('Выберите действие\n')
        if choice == '1':
            entered_username = input('Введите ваше имя:\n')
            entered_nickname = input('Введите ваше никнейм:\n')
            registration(entered_username, entered_nickname)

        elif choice == '2':
            entered_username = input('Введите ваше имя:\n')
            entered_password = input('Введите ваш пароль:\n')
            auth = Authorization(entered_username, entered_password)
            if not auth.is_authorization():
                print('Неверное имя либо пароль, попробуйте снова')
                continue
            print('Добро пожаловать в викторину!')
            questions = Question.questions()
            quiz = Quiz(questions)

            for question in questions:
                print(question.__str__())

                for index, variants in enumerate(question.variants):
                    print(f'{index}. {variants}')

                user_answer = int(input('Введите ваш ответ (цифрой):\n'))

                if quiz.is_true_answer(question, user_answer):
                    quiz.add_points(question)
                    auth.add_points_total(question)
                    print('Да, это верный ответ!')
                else:
                    print(f'Ответ не верный :(\nПравильный ответ -- {question.answer}')

                print(f'Ваше количество баллов: {quiz.total_points}')

            print('Конец! Спасибо за игру')

        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Неверно ввели цифру, попробуйте еще раз.')
            continue


if __name__ == '__main__':
    main()
