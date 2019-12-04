from typing import Tuple, Iterator
from sys import argv
from contract import JourneyReporter
from journey import Journey
from movement import Movement


class ManhattanReporter(set, JourneyReporter):
    def record_step(self, point: Tuple[int, int]):
        self.add(point)

    def distance_to_nearest_intersection(self, reporter: JourneyReporter) -> Tuple[int, int]:
        assert(isinstance(reporter, ManhattanReporter))
        return min([self.get_distance(loc) for loc in self & reporter])

    def get_distance(self, point: Tuple[int, int]):
        return abs(point[0]) + abs(point[1])


def main(resource_path):
    with open(resource_path, 'r') as fd:
         l = Journey.loads(ManhattanReporter(), fd.readline())
         r = Journey.loads(ManhattanReporter(), fd.readline())
         print(l.distance_to_nearest_intersection(r))


if __name__ == "__main__":
    main(argv[-1])
