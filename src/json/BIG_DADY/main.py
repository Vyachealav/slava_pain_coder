import os

from db.quiz_db import JsonQuizDB
from db.user_db import JsonUserDB
from ui.menu_ui import ConsoleMenuUI
from ui.user_ui import console_user_ui
from user.auth import Authorization, Registration

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_QUIZ_PATH = f'{DIR}/data/data.json'
JSON_USERS_PATH = f'{DIR}/data/users.json'

# Инициализация баз данных и других компонентов
quiz_db = JsonQuizDB(JSON_QUIZ_PATH)
user_db = JsonUserDB(JSON_USERS_PATH)
registration = Registration(console_user_ui, user_db)
authorization = Authorization(console_user_ui, user_db)
menu_ui = ConsoleMenuUI(registration, authorization, user_db, quiz_db)
# Запуск главного меню
while True:
    if menu_ui.display_main_menu() == 1:
        break
