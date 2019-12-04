from typing import Tuple, Iterator
from sys import argv
from contract import JourneyReporter
from journey import Journey
from movement import Movement


class StepCountReporter(dict, JourneyReporter):
    def __init__(self):
        self._step_count = 0

    def record_step(self, point: Tuple[int, int]):
        self._step_count += 1
        if point not in self:
            self[point] = self._step_count

    def __and__(self, reporter: JourneyReporter):
        assert(isinstance(reporter, StepCountReporter))
        return self.keys() & reporter.keys()

    def distance_to_nearest_intersection(self, reporter: JourneyReporter) -> Tuple[int, int]:
        assert(isinstance(reporter, StepCountReporter))
        return min([self.get_distance(loc) + reporter.get_distance(loc) for loc in self & reporter])

    def get_distance(self, point: Tuple[int, int]):
        return self.get(point)


def main(resource_path):
    with open(resource_path, 'r') as fd:
         l = Journey.loads(StepCountReporter(), fd.readline())
         r = Journey.loads(StepCountReporter(), fd.readline())
         print(l.distance_to_nearest_intersection(r))


if __name__ == "__main__":
    main(argv[-1])
