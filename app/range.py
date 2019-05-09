from collections import defaultdict


class Range:

    def __init__(self, area, x, y):
        self.areas = defaultdict(list)
        self.space = [x, y]
        self.areas[(x, y)].append(area)

    def add(self, area, x, y):
        first = self.space[0]
        last = self.space[-1]
        if y < first:
            self.space = [x, y] + self.space
            self.areas[(x, y)] = [area]
        elif x > last:
            self.space = self.space + [x, y]
            self.areas[(x, y)] = [area]

