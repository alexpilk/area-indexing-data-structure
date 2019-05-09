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


def test_area_inserted_after():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(50, 20, 5, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 40, 45, 55]
    assert main_range.areas == {(-20, 40): [area_1], (45, 55): [area_2]}


def test_area_inserted_touching_right_left():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(-30, 20, 10, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-40, -20, 40]
    assert main_range.areas == {(-20, 40): [area_1], (-40, -20): [area_2]}


def test_area_inserted_touching_right_right():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(0, 20, 40, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-40, -20, 40]
    assert main_range.areas == {(-20, 40): [area_1, area_2], (-40, -20): [area_2]}


def test_area_inserted_touching_left_left():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(0, 20, 20, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 20, 40]
    assert main_range.areas == {(-20, 20): [area_1, area_2], (20, 40): [area_1]}


def test_area_inserted_touching_left_right():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(50, 20, 10, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 40, 60]
    assert main_range.areas == {(-20, 40): [area_1], (40, 60): [area_2]}


def test_area_inserted_crossing_on_the_left():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(-30, 20, 20, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-50, -20, -10, 40]
    assert main_range.areas == {(-50, -20): [area_2], (-20, -10): [area_1, area_2], (-10, 40): [area_1]}


def test_area_inserted_crossing_on_the_right():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(30, 20, 20, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 10, 40, 50]
    assert main_range.areas == {(-20, 10): [area_1], (10, 40): [area_1, area_2], (40, 50): [area_2]}


def test_area_inserted_crossing_on_both_sides():
    main_area = Area(10, 20, 30, 'Main')
    left_cross = Area(-30, 20, 20, 'Left Cross')
    right_cross = Area(30, 20, 20, 'Right Cross')
    main_range = Range(main_area, main_area.min_lat, main_area.max_lat)
    main_range.add(left_cross, left_cross.min_lat, left_cross.max_lat)
    main_range.add(right_cross, right_cross.min_lat, right_cross.max_lat)
    assert main_range.space == [-50, -20, -10, 10, 40, 50]
    assert main_range.areas == {
        (-50, -20): [left_cross],
        (-20, -10): [main_area, left_cross],
        (-10, 10): [main_area],
        (10, 40): [main_area, right_cross],
        (40, 50): [right_cross]
    }


def test_area_inserted_crossing_on_both_sides_and_the_middle():
    main_area = Area(0, 20, 20, 'Main')
    left_cross = Area(-20, 20, 30, 'Left Cross')
    right_cross = Area(20, 20, 30, 'Right Cross')
    main_range = Range(main_area, main_area.min_lat, main_area.max_lat)
    main_range.add(left_cross, left_cross.min_lat, left_cross.max_lat)
    main_range.add(right_cross, right_cross.min_lat, right_cross.max_lat)
    assert main_range.space == [-50, -20, -10, 10, 20, 50]
    assert main_range.areas == {
        (-50, -20): [left_cross],
        (-20, -10): [main_area, left_cross],
        (-10, 10): [main_area, left_cross, right_cross],
        (10, 20): [main_area, right_cross],
        (20, 50): [right_cross]
    }


def test_area_inserted_inside():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(10, 20, 10, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 0, 20, 40]
    assert main_range.areas == {(-20, 0): [area_1], (0, 20): [area_1, area_2], (20, 40): [area_1]}


def test_area_inserted_outside():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(10, 20, 40, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-30, -20, 40, 50]
    assert main_range.areas == {(-30, -20): [area_2], (-20, 40): [area_1, area_2], (40, 50): [area_2]}


def test_area_inserted_aligns():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(10, 20, 30, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 40]
    assert main_range.areas == {(-20, 40): [area_1, area_2]}

