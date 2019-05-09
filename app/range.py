from collections import defaultdict
import bisect

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
        else:
            left_index = bisect.bisect_left(self.space, start)
            if self.space[left_index] == start:
                start_index = left_index
            elif left_index == 0:
                start_index = left_index
                self.space.insert(0, start)
            else:
                prev_el = self.space[left_index - 1]
                next_el = self.space[left_index]
                areas = self.areas.pop((prev_el, next_el))
                self.space.insert(left_index, start)
                self.areas[(prev_el, start)] = areas
                self.areas[(start, next_el)] = list(areas)
                start_index = left_index

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
                    areas = self.areas.pop((prev_el, next_el))
                    self.space.insert(right_index, end)
                    self.areas[(prev_el, end)] = areas
                    self.areas[(end, next_el)] = list(areas)
                    end_index = right_index

            for i in range(start_index, end_index):
                self.areas[(self.space[i], self.space[i + 1])].append(area)

    def _add_before(self, area, start, end):
        self.space = [start, end] + self.space
        self.areas[(start, end)] = [area]

    def _add_after(self, area, start, end):
        self.space = self.space + [start, end]
        self.areas[(start, end)] = [area]
