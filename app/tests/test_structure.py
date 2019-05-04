from app.tests.fixtures import area_index


def test_bulk_create(area_index):
    area_index.bulk_create([(-24.5, 134.8, 20, 'Australia')])


def test_query(area_index):
    assert area_index.query(0, 0) == []
