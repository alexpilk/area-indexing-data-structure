from app.structure.base import BaseAreaIndex


class DuplicateIds(Exception):
    pass


class SimpleAreaIndex(BaseAreaIndex):

    def __init__(self):
        self.areas = []

    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.

        >>> SimpleAreaIndex().bulk_create([(-24.5, 134.8, 20, 'Australia')])
        """
        self.areas = self._create_areas(areas)

    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: list

        >>> SimpleAreaIndex().query(0.0, 0.0)
        set()

        """
        return self._find_areas(self.areas, lat, long)
