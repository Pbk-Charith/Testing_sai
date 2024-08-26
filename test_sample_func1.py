import sample_func
import pytest
import sys
@pytest.mark.skipif(sys.version_info < (3, 12), reason="do not run add test number")
def test_add():
    assert sample_func.add(5, 3) == 8
    assert sample_func.add(5) == 7
    print(sample_func.add(5, 3), '*****')


def test_product():
    assert sample_func.product(5, 3) == 15
    assert sample_func.product(6) == 12


# def test_add_strings():
#     result = sample_func.add('Charith ','World')
#     assert result == 'Charith World'
#     assert type(result) is str
#     assert 'Charith ' in result


def test_product_strings():
    assert sample_func.product('Charith ',2) == 'Charith Charith '
    answer = sample_func.product('Charith ')
    assert answer == 'Charith Charith '
    assert type(answer) is str
    assert 'Charith ' in answer

def test_multiply_strings():
    assert sample_func.product('Cherry ',2) == 'Cherry Cherry '
    answer = sample_func.product('Cherry ')
    assert answer == 'Cherry Cherry '
    assert type(answer) is str
    assert 'Cherry ' in answer 