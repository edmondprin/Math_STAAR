from math_elem import generate_question_mult, generate_question_add, max_iters_mult, max_iters_add
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
    assert 0 < add_data[0] <= 100 and 0 < add_data[1] <= 100
    assert isinstance(add_data, tuple)
    for number in add_data:
        assert isinstance(number, int)

def test_max_iters_mult():
    range_down, range_up, test_iter = max_iters_mult()
    assert test_iter == (range_up * (range_up+range_down) / 2)
    assert isinstance(test_iter, int)
    if range_up == 10 and range_down == 1:
        test_iter == 55

def test_max_iters_add():
    range_down, range_up, test_iter = max_iters_add()
    if range_up == 100:
        test_iter == 5050
    if range_up == 50:
        test_iter == 1275