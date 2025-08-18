import os
import json

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = f'{DIR}/data/data.json'
JSON_USERS_PATH = f'{DIR}/data/users.json'


def read_json_data_file() -> None:
    if os.stat(JSON_PATH).st_size:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []


def read_json_users_file() -> None:
    if os.stat(JSON_USERS_PATH).st_size:
        with open(JSON_USERS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []
