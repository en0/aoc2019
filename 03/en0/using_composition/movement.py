from typing import Tuple, Generator


class Movement:
    def __init__(self, direction: str, distance: int):
        self.distance = distance
        self._move_one = {
            "U": self._up,
            "D": self._down,
            "R": self._right,
            "L": self._left
        }[direction]

    def path(self, origin: Tuple[int, int]) -> Generator[Tuple[int, int], None, None]:
        point = origin
        for i in range(self.distance):
            point = self._move_one(point)
            yield point

    def _up(self, point):
        x, y = point
        return (x, y+1)

    def _down(self, point):
        x, y = point
        return (x, y-1)

    def _left(self, point):
        x, y = point
        return (x-1, y)

    def _right(self, point):
        x, y = point
        return (x+1, y)

    @classmethod
    def loads(cls, movement: str):
        return cls(movement[0], int(movement[1:]))
