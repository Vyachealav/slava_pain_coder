# Придумать и написать свои тесты к программе из урока
# (В ЗАДАНИИ БЫЛО НАПИСАНО НА TEST UNIT, Я СДЕЛАЛ НА PYTEST, ИЗНАЧАЛЬНО БЫЛО ТОЛЬКО ДВА ПЕРВЫХ ТЕСТА)
from tests.task_1.count_vowels_and_consonants import count_vowels_and_consonants, is_russian_word


class TestCVAC:
    """Тесты для функции count_vowels_and_consonants"""

    def test_count_vowels_and_consonants(self):
        """Тестируем слово -- химик"""
        assert count_vowels_and_consonants('химик') == [2, 3]

    def test_count_vowels_and_consonants_with_upper_case(self):
        """Тестируем на верхний регистр"""
        assert count_vowels_and_consonants('ХИМИК') == [2, 3]

    def test_hard_and_soft_sign(self):
        """Тестируем слово на ъ и ь знаки, чтобы они не добавлялись ни к гласным, ни к согласным"""
        assert count_vowels_and_consonants('подъезд') == [2, 4]
        assert count_vowels_and_consonants('рысь') == [1, 2]

    def test_count_vowels_and_consonants_input_ru(self):
        """Тестируем ввод на иностранном языке, принимаем только кириллицу"""
        assert not is_russian_word('black')
