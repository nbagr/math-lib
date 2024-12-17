from scripts.figures import circle_perimeter, circle_area, square_area, \
    square_perimeter, triangle_perimeter, rectangle_area, rectangle_perimeter


def test_circle_area():
    assert circle_area(3) == 28.27
    assert circle_area(10) == 314.16
    assert circle_area(0) is None


def test_circle_perimeter():
    assert circle_perimeter(3) == 18.85
    assert circle_perimeter(10) == 62.83
    assert circle_perimeter(0) is None


def test_square_perimeter():
    assert square_perimeter(3) == 12
    assert square_perimeter(10) == 40
    assert square_perimeter(0) is None


def test_square_area():
    assert square_area(3) == 9
    assert square_area(10) == 100
    assert square_area(0) is None


def test_triangle_perimeter():
    assert triangle_perimeter(3, 3, 3) == 9
    assert triangle_perimeter(10, 7, 8) == 25
    assert triangle_perimeter(0) is None


def test_rectangle_perimeter():
    assert rectangle_perimeter(3, 3) == 12
    assert rectangle_perimeter(10, 7) == 34
    assert rectangle_perimeter(0, 10) is None


def test_rectangle_area():
    assert rectangle_area(3, 3) == 9
    assert rectangle_area(10, 7) == 70
    assert rectangle_area(0, 10) is None
