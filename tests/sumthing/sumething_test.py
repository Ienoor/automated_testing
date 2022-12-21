import pytest

from Classes.response import Response


@pytest.mark.development
def test_getting_code_status(get_users):
    Response(get_users).assert_status_code(200)


@pytest.mark.parametrize('first_number, second_number, result', [
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3),
    ('b', 'b', None),
])
def test_calculate(first_number, second_number, result, calculate):
    assert calculate(first_number, second_number) == result
