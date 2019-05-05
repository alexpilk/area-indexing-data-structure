from app.tests.fixtures import area_index
from app.structure import Area


def test_point_in_area(area_index):
    point = (-25, 15)
    area = Area(-20, 20, 20, 'Area 1')
    assert area_index._point_in_area(point, area)


def test_point_not_in_area(area_index):
    point = (0, 0)
    area = Area(-20, 20, 20, 'Area 1')
    assert not area_index._point_in_area(point, area)


def test_point_on_edge(area_index):
    point = (-20, 0)
    area = Area(-20, 20, 20, 'Area 1')
    assert area_index._point_in_area(point, area)


def test_query_point_in_one_area(area_index):
    area_index.bulk_create([(-10, 0, 10, 'Area 1'), (10, 0, 10, 'Area 2')])
    assert area_index.query(-10, 0) == ['Area 1']


def test_query_point_in_two_areas(area_index):
    area_index.bulk_create([(-10, 0, 10, 'Area 1'), (10, 0, 10, 'Area 2')])
    assert area_index.query(0, 0) == ['Area 1', 'Area 2']


def test_query_point_outside_two_areas(area_index):
    area_index.bulk_create([(-10, 0, 10, 'Area 1'), (10, 0, 10, 'Area 2')])
    assert area_index.query(0, 1) == []
