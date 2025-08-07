# Напишите программу, которая рекомендует, как одеться сегодня по погоде.
# В папке data лежат файлы вот в таком формате:

# <Название шмотки>
# <Тип шмотки>
# <Диапазон температур>

# Например:

# Шапка-ушанка
# Головной убор
# (-20, -5)

# или

# Шлепанцы
# Обувь
# (+20, +40)

# Программа спрашивает у пользователя, какая сейчас температура, а потом генерирует подходящий набор одежды,
# по одной шмотке каждого типа.
# Программа должна поддерживать добавление в папку data новых шмоток в виде текстовых файлов, в том числе,
# новых типов одежды, например: шарфы, футболки, перчатки. Заранее набор типов вещей не известен.
import os
import sys


class Clothes:
    def __init__(self, temperature: int, clothes: list[str | int]) -> None:
        self.temperature = temperature
        self.clothes = clothes

    @staticmethod
    def get_clothes(path, items) -> list[str | int]:
        clothes_array = []
        for item in items:
            with open(f'{path}/{item}', 'r', encoding='utf-8') as f:
                lines = [line.strip('()').strip() for line in f.readlines()]
                lines[2] = [int(num) for num in lines[2].split(', ')]
                clothes_array.append(lines)
        return clothes_array

    def print_clothes(self) -> None:
        suitable_clothes = [items for items in self.clothes if self.temperature in range(items[2][0], items[2][1])]
        if suitable_clothes:
            print('Предлагаем сегодня надеть:')
            for item in suitable_clothes:
                print(f'{item[0]} ({item[1]}) {item[2][0]}..{item[2][1]}')
        else:
            print('Вы в африке или антарктиде?')


class EditClothes:
    def __init__(self, clothing_name: str, clothing_type: str, temperature: str) -> None:
        self.clothing_name = clothing_name
        self.clothing_type = clothing_type
        self.temperature = temperature

    def add_clothes(self) -> None:
        items = len(os.listdir('data'))
        with open(f'data/item_{items + 1}', 'w', encoding='utf-8') as f:
            f.write(self.clothing_name + '\n')
            f.write(self.clothing_type + '\n')
            f.write(self.temperature)


def suggest_clothes() -> None:
    clothes_array = Clothes.get_clothes('data', os.listdir('data'))
    entered_temperature = int(input('Какая у вас сейчас температура?\n'))
    clothes = Clothes(entered_temperature, clothes_array)
    clothes.print_clothes()


def edit_clothes() -> None:
    clothing_name = input('Введите название одежды:\n')
    clothing_type = input('Введите тип одежды:\n')
    start_temperature = input('Введите начальный диапазон температуры:\n')
    end_temperature = input('Введите конечный диапазон тепературы:\n')
    temperature = f'({start_temperature}, {end_temperature})'
    editor = EditClothes(clothing_name, clothing_type, temperature)
    editor.add_clothes()


def show_menu() -> None:
    print("""
Добро пожаловать, выберите, что хотите сделать:
1. Подобрать одежду по погоде
2. Отредактировать приложение и добавить одежду
0. Выйти из приложения""")


def main() -> None:
    actions = {
        '1': suggest_clothes,
        '2': edit_clothes,
        '0': sys.exit,
    }
    while True:
        show_menu()
        choice = input()
        action = actions.get(choice)
        if action:
            action()
        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
