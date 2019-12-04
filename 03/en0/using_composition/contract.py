from typing import Tuple, Iterator
from abc import ABC, abstractmethod


class JourneyReporter(ABC):
    @abstractmethod
    def record_step(self, point: Tuple[int, int]):
        raise NotImplementedError()

    @abstractmethod
    def distance_to_nearest_intersection(self, reporter: "JourneyReporter") -> Tuple[int, int]:
        raise NotImplementedError()

    @abstractmethod
    def __and__(self, reporter: "JourneyReporter") -> Iterator[Tuple[int, int]]:
        raise NotImplementedError()

    @abstractmethod
    def get_distance(self, point: Tuple[int, int]):
        raise NotImplementedError()

