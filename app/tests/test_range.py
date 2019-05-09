from app.range import Range
from app.area import Area


def test_range_is_created():
    area = Area(10, 20, 30, 'Area 1')
    main_range = Range(area, area.min_lat, area.max_lat)
    assert main_range.space == [-20, 40]
    assert main_range.areas == {(-20, 40): [area]}


def test_area_inserted_before():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(-30, 20, 5, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-35, -25, -20, 40]
    assert main_range.areas == {(-20, 40): [area_1], (-35, -25): [area_2]}
