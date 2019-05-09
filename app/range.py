from collections import defaultdict


class Range:

    def __init__(self, area, start, end):
        self.areas = defaultdict(list)
        self.space = [start, end]
        self.areas[(start, end)].append(area)

    def add(self, area, start, end):
        first = self.space[0]
        last = self.space[-1]
        if end < first:
            self._add_before(area, start, end)
        elif start > last:
            self._add_after(area, start, end)

    def _add_before(self, area, start, end):
        self.space = [start, end] + self.space
        self.areas[(start, end)] = [area]

    def _add_after(self, area, start, end):
        self.space = self.space + [start, end]
        self.areas[(start, end)] = [area]
