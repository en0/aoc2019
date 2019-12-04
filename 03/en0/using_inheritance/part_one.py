from sys import argv


class Journey(set):

    def __init__(self):
        super(Journey, self).__init__()
        self._loc = (0, 0)

    def walk(self, movement):
        self._walk(movement[0], int(movement[1:]))

    def _walk(self, direction, steps):
        for i in range(steps):
            self._step(direction)

    def _step(self, direction):
        x, y = self._loc
        if direction == "U":
            self.set_location((x, y + 1))
        elif direction == "D":
            self.set_location((x, y - 1))
        elif direction == "L":
            self.set_location((x - 1, y))
        elif direction == "R":
            self.set_location((x + 1, y))

    def set_location(self, point: tuple):
        self._loc = point
        self.add(point)

    def get_location(self) -> tuple:
        return self._loc

    @classmethod
    def loads(cls, movements: str) -> "Journey":
        ret = cls()
        for movement in movements.split(","):
            ret.walk(movement)
        return ret;


def main(resource_path):
    with open(resource_path, 'r') as fd:
        r = Journey.loads(fd.readline())
        l = Journey.loads(fd.readline())
        ans = sorted([abs(x)+abs(y) for x, y in r & l])[0]
        print(ans)

if __name__ == "__main__":
    main(argv[-1])
