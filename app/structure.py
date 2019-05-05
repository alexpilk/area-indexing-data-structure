class AreaIndex:

    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.

        >>> AreaIndex().bulk_create([(-24.5, 134.8, 20, 'Australia')])
        """

    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: list

        >>> AreaIndex().query(0.0, 0.0)
        []

        """
        return []

    def _point_in_area(self, point, area):
        lat = area[0]
        long = area[1]
        radius = area[2]
        return (point[0] - lat) ** 2 + (point[1] - long) ** 2 <= radius ** 2
