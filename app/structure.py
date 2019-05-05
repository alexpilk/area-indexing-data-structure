from dataclasses import dataclass
from numbers import Real as RealNumber


@dataclass
class Area:
    latitude: RealNumber
    longitude: RealNumber
    radius: RealNumber
    id: object


class AreaIndex:

    def __init__(self):
        self.areas = {}

    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.

        >>> AreaIndex().bulk_create([(-24.5, 134.8, 20, 'Australia')])
        """
        for area in areas:
            area = Area(*area)
            self.areas[area.id] = area

    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: list

        >>> AreaIndex().query(0.0, 0.0)
        []

        """
        return [area_id for area_id, area in self.areas.items() if self._point_in_area((lat, long), area)]

    def _point_in_area(self, point, area):
        latitude_delta = point[0] - area.latitude
        longitude_delta = point[1] - area.longitude
        return latitude_delta ** 2 + longitude_delta ** 2 <= area.radius ** 2
