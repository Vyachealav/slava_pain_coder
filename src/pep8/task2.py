# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
# Входные данные: Положительное целое число.
# Выходные данные: Целое число (0-9).


def max_digit(number: int) -> int:
    number_array = list(str(number))
    return max(list(map(int, number_array)))


number = int(input('Введите число:\n'))
print(f'Наибольшая цифра в числе: {max_digit(number)}')
