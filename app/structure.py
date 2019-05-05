from dataclasses import dataclass
from numbers import Real as RealNumber


class DuplicateIds(Exception):
    pass


@dataclass
class Area:
    latitude: RealNumber
    longitude: RealNumber
    radius: RealNumber
    id: object


class AreaIndex:

    def __init__(self):
        self.areas = []

    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.

        >>> AreaIndex().bulk_create([(-24.5, 134.8, 20, 'Australia')])
        """
        if len({area[3] for area in areas}) < len(areas):
            raise DuplicateIds('Multiple areas have same IDs')

        self.areas = [Area(*area) for area in areas]

    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: list

        >>> AreaIndex().query(0.0, 0.0)
        []

        """
        return [area.id for area in self.areas if self._point_in_area((lat, long), area)]

    @staticmethod
    def _point_in_area(point, area):
        latitude_delta = point[0] - area.latitude
        longitude_delta = point[1] - area.longitude
        return latitude_delta ** 2 + longitude_delta ** 2 <= area.radius ** 2
