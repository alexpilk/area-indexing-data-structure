from pytest import fixture
from app.structure import AreaIndex


@fixture
def area_index():
    return AreaIndex()


def test_bulk_create(area_index):
    area_index.bulk_create([(-24.5, 134.8, 20, 'Australia')])
