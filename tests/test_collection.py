from scripts.collection import min, max, average, sort


def test_min():
    assert min([24, 10, 7, 6, 0]) == 0
    assert min([13, 0, 1, 1, 6]) == 0
    assert min([52, 23, 15, 20, 40]) == 15
    assert min([92, -1, 73, -20, 0]) == -20
    assert min([1]) == 1
    assert min([]) is None


def test_max():
    assert max([24, 10, 7, 6, 0]) == 24
    assert max([13, 0, 1, 1, 6]) == 13
    assert max([52, 23, 15, 20, 40]) == 52
    assert max([-92, -1, -73, -20]) == -1
    assert max([1]) == 1
    assert max([-92, -1, -73, -20, 0]) == 0
    assert max([]) is None


def test_average():
    assert average([24, 10, 7, 6, 0]) == 9.4
    assert average([13, 0, 1, 1, 6]) == 4.2
    assert average([52, 23, 15, 20, 40]) == 30
    assert average([92, -1, 73, -20, 0]) == 28.8
    assert average([1]) == 1
    assert average([]) is None


def test_sort():
    assert sort([24, 10, 7, 6, 0]) == [0, 6, 7, 10, 24]
    assert sort([13, 0, 1, 1, 6]) == [0, 1, 1, 6, 13]
    assert sort([52, 23, 15, 20, 40]) == [15, 20, 23, 40, 52]
    assert sort([92, -1, 73, -20, 0]) == [-20, -1, 0, 73, 92]
    assert sort([1]) == [1]
    assert sort([]) is None
