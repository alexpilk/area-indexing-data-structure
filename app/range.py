from collections import defaultdict


class Range:

    def __init__(self, area, x, y):
        self.areas = defaultdict(list)
        self.space = [x, y]
        self.areas[(x, y)].append(area)
