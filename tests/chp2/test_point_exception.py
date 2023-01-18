from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest
# good case


def test_point():
    point1 = Point("Name", 14.25, 21.5)
    assert (point1.get_lat_long() == (14.25, 21.5))

# exception case with name of city


def test_point_exception_city():

    with pytest.raises(TypeError) as exp:
        Point(22, 35, 56)
    assert (str(exp.value) == "wrong type")


def test_point_exception_long_lat():

    with pytest.raises(ValueError) as exp:
        Point("hanoi", -15, 256)
    assert (str(exp.value) == "wrong input")
