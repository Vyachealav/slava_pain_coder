# Задания к уроку 1
# 3 points
# Проверить является ли число четным или нет. Ваша функция должна возвращать True если число четное, и False если число не четное.
# Входные данные: Целое число.
# Выходные данные: Логический тип.
def is_even_numbered(number: int) -> bool:
    return number % 2 == 0


number = int(input('Введите число:\n'))
if is_even_numbered(number):
    print('Четное число')
else:
    print('Нечетное число')
