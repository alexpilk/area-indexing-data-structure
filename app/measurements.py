import random
from time import time

from app.structure import SimpleAreaIndex, RangeBasedAreaIndex

MIN_LAT = -90
MAX_LAT = 90
MIN_LONG = -180
MAX_LONG = 180
MIN_RADIUS = 1
MAX_RADIUS = 100
SIZE = 100000


def generate_areas():
    return [
        (
            random.randint(MIN_LAT, MAX_LAT),
            random.randint(MIN_LONG, MAX_LONG),
            random.randint(MIN_RADIUS, MAX_RADIUS),
            str(i)
        ) for i in range(100)
    ]


def query(area_index, points):
    for i in range(SIZE):
        area_index.query(*points[i])


def measure(action, message):
    start = time()
    action()
    end = time()
    print(message.format(end - start))


if __name__ == '__main__':
    random.seed(0)

    areas = generate_areas()
    simple_area_index = SimpleAreaIndex()
    range_based_index = RangeBasedAreaIndex()

    measure(lambda: simple_area_index.bulk_create(areas), 'Initializing simple area index: {}')
    measure(lambda: range_based_index.bulk_create(areas), 'Initializing range based index: {}')

    points_to_query = [(random.randint(MIN_LAT, MAX_LAT), random.randint(MIN_LONG, MAX_LONG)) for i in range(SIZE)]

    measure(lambda: query(simple_area_index, points_to_query), 'Querying simple area index: {}')
    measure(lambda: query(range_based_index, points_to_query), 'Querying range based index: {}')


# Initializing simple area index: 0.0009999275207519531
# Initializing range based index: 0.008000612258911133
# Querying simple area index: 20.059147357940674
# Querying range based index: 12.539716958999634
