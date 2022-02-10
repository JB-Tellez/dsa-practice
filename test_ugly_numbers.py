from ugly_numbers import ugly_numbers


def test_one():
    actual = ugly_numbers(1)
    expected = 1
    assert actual == expected


def test_two():
    actual = ugly_numbers(2)
    expected = 2
    assert actual == expected


def test_seven():
    actual = ugly_numbers(7)
    expected = 8
    assert actual == expected


def test_ten():
    actual = ugly_numbers(10)
    expected = 12
    assert actual == expected


def test_fifteen():
    actual = ugly_numbers(15)
    expected = 24
    assert actual == expected


# def test_one_hundred_fifty():
#     actual = ugly_numbers(150)
#     expected = 5832
#     assert actual == expected
