import sample_func
import pytest

@pytest.mark.number
def test_add():
    assert sample_func.add(5, 3) == 8
    assert sample_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert sample_func.product(5, 3) == 15
    assert sample_func.product(6) == 12

# @pytest.mark.strings
# def test_strings():
#     result = sample_func.add('Charith ','World')
#     assert result == 'Charith World'
#     assert type(result) is str
#     assert 'Charith ' in result

# @pytest.mark.strings
# def test_strings():
#     assert sample_func.product('Charith ',2) == 'Charith Charith '
#     answer = sample_func.product('Charith ')
#     assert answer == 'Charith Charith '
#     assert type(answer) is str
#     assert 'Charith ' in answer 