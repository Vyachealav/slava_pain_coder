# 1. Напишите математическую функцию со знаками “+”, “-”, “*” и “/”, которая умеет принимать три параметра 1-е число,
# 2-е число и один из четырех математических знаков.
# 2. Распишите тесты для этой функции
import pytest
from calculator import calculator


class TestCalculator:
    @pytest.mark.parametrize(
        'a, b, expected_sum',
        [
            (1, 2, 3),
            (-7, 7, 0),
            (0, 0, 0),
            (5.25, 0.75, 6),
        ],
    )
    def test_sum(self, a, b, expected_sum):
        assert calculator(a, b, '+') == expected_sum

    @pytest.mark.parametrize(
        'a, b, expected_subtraction',
        [
            (1, 2, -1),
            (7, 7, 0),
            (0, 0, 0),
            (-5.25, 0.25, -5.5),
        ],
    )
    def test_subtraction(self, a, b, expected_subtraction):
        assert calculator(a, b, '-') == expected_subtraction

    @pytest.mark.parametrize(
        'a, b, expected_divide',
        [
            (4, 2, 2),
            (7, 7, 1),
            (-9, 3, -3),
            (5, 2, 2.5),
        ],
    )
    def test_divide(self, a, b, expected_divide):
        assert calculator(a, b, '/') == expected_divide

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator(10, 0, '/')

    @pytest.mark.parametrize(
        'a, b, expected_multiplication',
        [
            (4, 2, 8),
            (7, 7, 49),
            (-9, 3, -27),
            (2.5, 2, 5),
            (2.5, 0, 0),
        ],
    )
    def test_multiplication(self, a, b, expected_multiplication):
        assert calculator(a, b, '*') == expected_multiplication
