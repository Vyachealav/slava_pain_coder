# 1. Напишите математическую функцию со знаками “+”, “-”, “*” и “/”, которая умеет принимать три параметра 1-е число,
# 2-е число и один из четырех математических знаков.
# 2. Распишите тесты для этой функции


def calculator(first_number, second_number, sign):
    if sign == '+':
        return first_number + second_number
    if sign == '-':
        return first_number - second_number
    if sign == '*':
        return first_number * second_number
    if sign == '/':
        return first_number / second_number
    return 'Ошибка, такой операции не существует'


def main():
    print(calculator(1, 2, '+'))


if __name__ == '__main__':
    main()
