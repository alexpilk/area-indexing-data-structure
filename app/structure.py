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
        """
        return []
