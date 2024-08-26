import sample_func1
import pytest

@pytest.mark.parametrize('num1, num2, result',
                         [
                             (1, 2, 3),
                             ('Hello ', 'World', 'Hello World'),
                             (10.5, 20.5, 31)
                         ]
                         )

def test_add(num1, num2, result):
    assert sample_func1.add(num1, num2) == result