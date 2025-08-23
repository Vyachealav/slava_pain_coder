from dataclasses import dataclass


@dataclass
class RegistrationForm:
    username: str
    nickname: str
    password: str


@dataclass
class LoginForm:
    username: str
    password: str
