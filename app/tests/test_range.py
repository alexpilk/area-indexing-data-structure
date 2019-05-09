from app.area import Area
from app.range import Range


def test_range_is_created():
    area = Area(10, 20, 30, 'Area 1')
    main_range = Range(area, area.min_lat, area.max_lat)
    assert main_range.space == [-20, 40]
    assert main_range.areas == {(-20, 40): {area}}


def test_area_inserted_before():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(-30, 20, 5, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-35, -25, -20, 40]
    assert main_range.areas == {(-20, 40): {area_1}, (-35, -25): {area_2}}


def test_area_inserted_after():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(50, 20, 5, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 40, 45, 55]
    assert main_range.areas == {(-20, 40): {area_1}, (45, 55): {area_2}}


def test_area_inserted_between():
    left = Area(-20, 20, 10, 'Left')
    right = Area(20, 20, 10, 'Right')
    middle = Area(0, 20, 5, 'Middle')
    main_range = Range(left, left.min_lat, left.max_lat)
    main_range.add(right, right.min_lat, right.max_lat)
    main_range.add(middle, middle.min_lat, middle.max_lat)
    assert main_range.space == [-30, -10, -5, 5, 10, 30]
    assert main_range.areas == {
        (-30, -10): {left},
        (-10, -5): set(),
        (-5, 5): {middle},
        (5, 10): set(),
        (10, 30): {right}
    }


def test_area_inserted_touching_right_left():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(-30, 20, 10, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-40, -20, 40]
    assert main_range.areas == {(-20, 40): {area_1}, (-40, -20): {area_2}}


def test_area_inserted_touching_right_right():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(0, 20, 40, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-40, -20, 40]
    assert main_range.areas == {(-20, 40): {area_1, area_2}, (-40, -20): {area_2}}


def test_area_inserted_touching_left_left():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(0, 20, 20, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 20, 40]
    assert main_range.areas == {(-20, 20): {area_1, area_2}, (20, 40): {area_1}}


def test_area_inserted_touching_left_right():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(50, 20, 10, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 40, 60]
    assert main_range.areas == {(-20, 40): {area_1}, (40, 60): {area_2}}


def test_area_inserted_touching_on_all_sides():
    main_area = Area(0, 20, 10, 'Area 1')
    left = Area(-20, 20, 10, 'Area 2')
    left_right = Area(-6, 20, 4, 'Area 3')
    right_left = Area(6, 20, 4, 'Area 4')
    right = Area(20, 20, 10, 'Area 5')
    main_range = Range(main_area, main_area.min_lat, main_area.max_lat)
    main_range.add(left, left.min_lat, left.max_lat)
    main_range.add(left_right, left_right.min_lat, left_right.max_lat)
    main_range.add(right_left, right_left.min_lat, right_left.max_lat)
    main_range.add(right, right.min_lat, right.max_lat)
    assert main_range.space == [-30, -10, -2, 2, 10, 30]
    assert main_range.areas == {
        (-30, -10): {left},
        (-10, -2): {main_area, left_right},
        (-2, 2): {main_area},
        (2, 10): {main_area, right_left},
        (10, 30): {right}
    }


def test_area_inserted_crossing_on_the_left():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(-30, 20, 20, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-50, -20, -10, 40]
    assert main_range.areas == {(-50, -20): {area_2}, (-20, -10): {area_1, area_2}, (-10, 40): {area_1}}


def test_area_inserted_crossing_on_the_right():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(30, 20, 20, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 10, 40, 50]
    assert main_range.areas == {(-20, 10): {area_1}, (10, 40): {area_1, area_2}, (40, 50): {area_2}}


def test_area_inserted_crossing_on_both_sides():
    main_area = Area(10, 20, 30, 'Main')
    left_cross = Area(-30, 20, 20, 'Left Cross')
    right_cross = Area(30, 20, 20, 'Right Cross')
    main_range = Range(main_area, main_area.min_lat, main_area.max_lat)
    main_range.add(left_cross, left_cross.min_lat, left_cross.max_lat)
    main_range.add(right_cross, right_cross.min_lat, right_cross.max_lat)
    assert main_range.space == [-50, -20, -10, 10, 40, 50]
    assert main_range.areas == {
        (-50, -20): {left_cross},
        (-20, -10): {main_area, left_cross},
        (-10, 10): {main_area},
        (10, 40): {main_area, right_cross},
        (40, 50): {right_cross}
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
        (-50, -20): {left_cross},
        (-20, -10): {main_area, left_cross},
        (-10, 10): {main_area, left_cross, right_cross},
        (10, 20): {main_area, right_cross},
        (20, 50): {right_cross}
    }


def test_area_inserted_inside():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(10, 20, 10, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 0, 20, 40]
    assert main_range.areas == {(-20, 0): {area_1}, (0, 20): {area_1, area_2}, (20, 40): {area_1}}


def test_area_inserted_outside():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(10, 20, 40, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-30, -20, 40, 50]
    assert main_range.areas == {(-30, -20): {area_2}, (-20, 40): {area_1, area_2}, (40, 50): {area_2}}


def test_area_inserted_aligns():
    area_1 = Area(10, 20, 30, 'Area 1')
    area_2 = Area(10, 20, 30, 'Area 2')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    main_range.add(area_2, area_2.min_lat, area_2.max_lat)
    assert main_range.space == [-20, 40]
    assert main_range.areas == {(-20, 40): {area_1, area_2}}


def test_query_not_found():
    area_1 = Area(0, 20, 10, 'Area 1')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    assert main_range.search(-11) == []
    assert main_range.search(11) == []


def test_query_found_in_one_area():
    area_1 = Area(0, 20, 10, 'Area 1')
    main_range = Range(area_1, area_1.min_lat, area_1.max_lat)
    assert main_range.search(0) == {area_1}
    assert main_range.search(-10) == {area_1}
    assert main_range.search(10) == {area_1}


def test_query_found_in_multiple_areas():
    main_area = Area(0, 20, 20, 'Main')
    left_cross = Area(-20, 20, 30, 'Left Cross')
    right_cross = Area(20, 20, 30, 'Right Cross')
    main_range = Range(main_area, main_area.min_lat, main_area.max_lat)
    main_range.add(left_cross, left_cross.min_lat, left_cross.max_lat)
    main_range.add(right_cross, right_cross.min_lat, right_cross.max_lat)
    assert main_range.search(-50) == {left_cross}
    assert main_range.search(-40) == {left_cross}
    assert main_range.search(-20) == {main_area, left_cross}
    assert main_range.search(-15) == {main_area, left_cross}
    assert main_range.search(-10) == {main_area, left_cross, right_cross}
    assert main_range.search(0) == {main_area, left_cross, right_cross}
    assert main_range.search(10) == {main_area, left_cross, right_cross}
    assert main_range.search(15) == {main_area, right_cross}
    assert main_range.search(20) == {main_area, right_cross}
    assert main_range.search(40) == {right_cross}
    assert main_range.search(50) == {right_cross}
