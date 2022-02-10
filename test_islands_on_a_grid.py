from islands_on_a_grid import count_islands


def test_islands_on_a_grid():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0],
    ]

    actual = count_islands(grid)

    expected = 4

    assert actual == expected


def test_islands_on_a_grid_empty():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    actual = count_islands(grid)

    expected = 0

    assert actual == expected


def test_islands_on_a_grid_():

    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0],
    ]

    actual = count_islands(grid)

    expected = 4

    assert actual == expected
