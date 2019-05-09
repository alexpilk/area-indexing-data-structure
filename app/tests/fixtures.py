from pytest import fixture

from app.structure import SimpleAreaIndex, RangeBasedAreaIndex


@fixture(params=[SimpleAreaIndex, RangeBasedAreaIndex])
def area_index(request):
    return request.param()
