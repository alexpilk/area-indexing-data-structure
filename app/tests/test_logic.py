from app.tests.fixtures import area_index


def test_point_in_area(area_index):
    point = (-25, 15)
    area = (-20, 20, 20, 'Area 1')
    assert area_index._point_in_area(point, area)


def test_point_not_in_area(area_index):
    point = (0, 0)
    area = (-20, 20, 20, 'Area 1')
    assert not area_index._point_in_area(point, area)


def test_point_on_edge(area_index):
    point = (-20, 0)
    area = (-20, 20, 20, 'Area 1')
    assert area_index._point_in_area(point, area)
