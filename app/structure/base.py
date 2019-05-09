from abc import ABC, abstractmethod

from app.area import Area


class DuplicateIds(Exception):
    pass


class BaseAreaIndex(ABC):

    @abstractmethod
    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.
        """

    @abstractmethod
    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: list
        """

    @staticmethod
    def _create_areas(areas):
        """
        Checks for duplicated area IDs and creates Area objects.

        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.
        :return: parsed areas
        :rtype: set(Area)
        """
        if len({area[3] for area in areas}) < len(areas):
            raise DuplicateIds('Multiple areas have same IDs')

        return {Area(*area) for area in areas}

    @classmethod
    def _find_areas(cls, areas, lat, long):
        """
        :param set(Area) areas: areas to check
        :param float lat:
        :param float long:
        :return: all areas with given point.
        :rtype: set(Area)
        """
        return {area.id for area in areas if cls._point_in_area((lat, long), area)}

    @staticmethod
    def _point_in_area(point, area):
        """
        Checks if given point is within given area.

        :param tuple(float) point: e.g. (0, 0)
        :param Area area:
        :rtype: bool
        """
        latitude_delta = point[0] - area.latitude
        longitude_delta = point[1] - area.longitude
        return latitude_delta ** 2 + longitude_delta ** 2 <= area.radius ** 2
