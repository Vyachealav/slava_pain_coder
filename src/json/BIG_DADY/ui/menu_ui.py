from core.abstract import QuizDBBase, UserModelBase
from core.game import Game
from ui.game_ui import ConsoleGameUI, console_game_ui
from user.abstract import UserDBBase
from user.auth import Authorization, Registration, UnknownUserError


class ConsoleMenuUI:
    def __init__(
        self,
        registration: Registration,
        authorization: Authorization,
        user_db: UserDBBase,
        quiz_db: QuizDBBase,
        game_ui: ConsoleGameUI = console_game_ui,
    ) -> None:
        self.registration = registration
        self.authorization = authorization
        self.user_db = user_db
        self.quiz_db = quiz_db
        self.game_ui = game_ui

    def display_main_menu(self) -> int:
        print('Добро пожаловать в игру!')
        print('1. Регистрация')
        print('2. Вход')
        print('3. Выход')
        choice = input('Выберите опцию: ')
        if choice == '1':
            self.register_user()
        elif choice == '2':
            self.login_user()
        elif choice == '3':
            return 1
        else:
            print('Неверный выбор. Пожалуйста, попробуйте снова.')
        return 0

    def register_user(self) -> None:
        user_model = self.registration.register()
        print(f'Пользователь {user_model.username} успешно зарегистрирован!')

    def login_user(self) -> None:
        try:
            user_model = self.authorization.login()
            if user_model:
                print(f'Добро пожаловать, {user_model.username}!')
                self.start_game(user_model)
        except UnknownUserError as e:
            print(e)

    def start_game(self, user_model: UserModelBase) -> None:
        print('Начинаем игру...')
        quiz = self.quiz_db.load_questions()
        game = Game(quiz, user_model, self.game_ui)
        game.start()
        self.user_db.save_user(user_model)
        print('Спасибо за игру! Ваши очки сохранены.')
