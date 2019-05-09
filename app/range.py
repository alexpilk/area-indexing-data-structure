import bisect
from collections import defaultdict


class Range:

    def __init__(self, area, start, end):
        self.areas = defaultdict(set)
        self.space = [start, end]
        self.areas[(start, end)].add(area)

    def add(self, area, start, end):
        first = self.space[0]
        last = self.space[-1]
        if end < first:
            self._add_before(area, start, end)
        elif start > last:
            self._add_after(area, start, end)
        else:
            start_index = self._add_left_side(start)
            end_index = self._add_right_side(end)

            for i in range(start_index, end_index):
                self.areas[(self.space[i], self.space[i + 1])].add(area)

    def _add_left_side(self, start):
        left_index = bisect.bisect_left(self.space, start)
        if self.space[left_index] == start:
            pass
        elif left_index == 0:
            self.space.insert(0, start)
        else:
            prev_el = self.space[left_index - 1]
            next_el = self.space[left_index]
            areas = self.areas.pop((prev_el, next_el), set())
            self.space.insert(left_index, start)
            self.areas[(prev_el, start)] = areas
            self.areas[(start, next_el)] = set(areas)
        return left_index

    def _add_right_side(self, end):
        right_index = bisect.bisect_right(self.space, end)
        if right_index == len(self.space):
            if self.space[-1] == end:
                end_index = right_index - 1
            else:
                end_index = right_index
                self.space.append(end)
        else:
            prev_el = self.space[right_index - 1]
            next_el = self.space[right_index]
            if prev_el == end:
                end_index = right_index - 1
            elif next_el == end:
                end_index = right_index
            else:
                areas = self.areas.pop((prev_el, next_el), set())
                self.space.insert(right_index, end)
                self.areas[(prev_el, end)] = areas
                self.areas[(end, next_el)] = set(areas)
                end_index = right_index
        return end_index

    def _add_before(self, area, start, end):
        self.space = [start, end] + self.space
        self.areas[(start, end)] = {area}

    def _add_after(self, area, start, end):
        self.space = self.space + [start, end]
        self.areas[(start, end)] = {area}

    def search(self, position):
        if position < self.space[0] or position > self.space[-1]:
            return []
        else:
            left_index = bisect.bisect_left(self.space, position)
            if left_index != 0:
                left_index -= 1
            right_index = left_index + 1
            left = self.space[left_index]
            right = self.space[right_index]
            if left == position and left != self.space[0]:
                return self.areas[self.space[left_index - 1], left] | self.areas[left, right]
            elif right == position and right != self.space[-1]:
                return self.areas[right, self.space[right_index + 1]] | self.areas[left, right]
            else:
                return self.areas[left, right]
