from math_elem import generate_question_mult, generate_question_add
# import random

def test_mult():
    # random.seed(1)
    mult_data = generate_question_mult()
    # assert mult_data == (3, 10, 30)
    assert len(mult_data) == 3
    assert 0 < mult_data[0] < 11 and 0 < mult_data[1] < 11
    assert mult_data[-1] == mult_data[0] * mult_data[1]
    assert isinstance(mult_data, tuple)
    for number in mult_data:
        assert isinstance(number, int)

def test_add():
    # random.seed(1)
    add_data = generate_question_add()
    # assert add_data == (18, 73, 91)
    assert len(add_data) == 3
    assert add_data[-1] == add_data[0] + add_data[1]
    assert 0 < add_data[0] < 100 and 0 < add_data[1] < 101
    assert isinstance(add_data, tuple)
    for number in add_data:
        assert isinstance(number, int)
