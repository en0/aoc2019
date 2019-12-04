from typing import Tuple
from movement import Movement
from contract import JourneyReporter


class Journey:

    _loc: Tuple[int, int]
    _reporter: JourneyReporter

    def __init__(self, reporter: JourneyReporter):
        self._loc = (0, 0)
        self._reporter = reporter

    def walk(self, movement: Movement):
        for step in movement.path(self._loc):
            self._reporter.record_step(step)
        self._loc = step

    def distance_to_nearest_intersection(self, journey: "Journey"):
        return self._reporter.distance_to_nearest_intersection(journey._reporter)

    @classmethod
    def loads(cls, reporter, movements: str) -> "Journey":
        ret = cls(reporter)
        for movement in movements.split(","):
            ret.walk(Movement.loads(movement))
        return ret;

