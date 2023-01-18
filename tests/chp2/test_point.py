from scripts.chp2.video2.mapmaker_start import Point


def test_point():
    point1 = Point("Name", 14.25, 21.5)
    assert (point1.get_lon_lat() == (14.25, 21.5))
