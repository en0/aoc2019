from sys import argv
from part_one import Journey


class TrackedJourney(Journey):

    def __init__(self):
        super(TrackedJourney, self).__init__()
        self._step_count = 0
        self._tracks = dict()

    def step_count_at(self, point: tuple) -> int:
        return self._tracks.get(point)

    def set_location(self, point: tuple):
        super(TrackedJourney, self).set_location(point)
        self._step_count += 1
        if point not in self._tracks:
            self._tracks[point] = self._step_count


def main(resource_path):
    with open(resource_path, 'r') as fd:
        r = TrackedJourney.loads(fd.readline())
        l = TrackedJourney.loads(fd.readline())
        ans = min([r.step_count_at(loc) + l.step_count_at(loc)
            for loc in r & l])
        print(ans)

if __name__ == "__main__":
    main(argv[-1])
