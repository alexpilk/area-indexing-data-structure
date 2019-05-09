from app.range import Range
from app.structure.base import BaseAreaIndex


class RangeBasedAreaIndex(BaseAreaIndex):

    def __init__(self):
        self.latitudes = None
        self.longitudes = None

    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.

        >>> RangeBasedAreaIndex().bulk_create([(-24.5, 134.8, 20, 'Australia')])
        """
        areas = self._create_areas(areas)
        first_area = areas.pop()
        self.latitudes = Range(first_area, first_area.min_lat, first_area.max_lat)
        self.longitudes = Range(first_area, first_area.min_long, first_area.max_long)
        for area in areas:
            self.latitudes.add(area, area.min_lat, area.max_lat)
            self.longitudes.add(area, area.min_long, area.max_long)

    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: set(Area)

        >>> RangeBasedAreaIndex().query(0.0, 0.0)
        set()

        """
        if self.longitudes and self.latitudes:
            possible_areas = self.latitudes.search(lat).union(self.longitudes.search(long))
            return self._find_areas(possible_areas, lat, long)
        else:
            return set()
