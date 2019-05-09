from app.range import Range
from app.area import Area


def test_range_is_created():
    area = Area(10, 20, 30, 'Area 1')
    main_range = Range(area, area.min_lat, area.max_lat)
    assert main_range.space == [-20, 40]
    assert main_range.areas == {(-20, 40): [area]}
