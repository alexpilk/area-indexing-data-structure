from pytest import fixture
from app.structure import AreaIndex


@fixture
def area_index():
    return AreaIndex()
