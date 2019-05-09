from app.area import Area


def test_area_is_created_correctly():
    area = Area(10, 20, 30, 'Area 1')
    assert area.latitude == 10
    assert area.longitude == 20
    assert area.radius == 30
    assert area.id == 'Area 1'
    assert area.min_lat == -20
    assert area.max_lat == 40
    assert area.min_long == -10
    assert area.max_long == 50
    assert repr(area) == 'Area "Area 1" at (10, 20) ± 30'
