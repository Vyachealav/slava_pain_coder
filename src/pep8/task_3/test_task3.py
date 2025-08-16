# Напишите тесты для программ “Как одеться сегодня по погоде”.
# Соответственно чтобы её протестить, нужно создать тестовый файл, и проверить,
# что с него корректно раскладывается по списку данные
import os
import pytest
import shutil
from task3 import Clothes


@pytest.fixture
def get_items_and_directory():
    if os.path.exists('temporary_dir'):
        shutil.rmtree('temporary_dir')
    os.mkdir('temporary_dir')
    current_directory = os.getcwd() + '/temporary_dir/'
    with open('temporary_dir/test', 'w', encoding='utf-8') as f:
        f.write('Толстовка' + '\n')
        f.write('Верхняя одежда ' + '\n')
        f.write('(-20, -5)')
    return current_directory, os.listdir(current_directory)


class TestClothes:
    def test_get_clothes(self, get_items_and_directory):
        current_directory = get_items_and_directory[0]
        items = get_items_and_directory[1]
        assert Clothes.get_clothes(current_directory, items) == [['Толстовка', 'Верхняя одежда', [-20, -5]]]
