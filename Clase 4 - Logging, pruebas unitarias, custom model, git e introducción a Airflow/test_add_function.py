from add_function import add_two_numbers

def test_add_two_numbers_positives():
    assert(add_two_numbers(2, 7) == 9)

def test_add_two_numbers_negatives():
    assert(add_two_numbers(-1, -2) == -3)

def test_add_one_number_and_zero():
    assert(add_two_numbers(3, 0) == 3) # wrong

def test_add_two_zeros():
    assert(add_two_numbers(0, 0) == 0)