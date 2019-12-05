from sys import argv
from typing import List
from abc import ABC, abstractmethod


class IValidator(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def test(self, char: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def finalize(self) -> bool:
        raise NotImplementedError()


class Validator:
    _validators: List[IValidator]
    def __init__(self, validators: List[IValidator] = None):
        self._validators = validators or []

    def add_validator(self, validator: IValidator):
        self._validators.append(validator)

    def test(self, value: str) -> bool:
        [v.reset() for v in self._validators]
        for char in value:
            if not all([v.test(char) for v in self._validators]):
                return False
        return all([v.finalize() for v in self._validators])


class IntegerValidator(IValidator):
    def reset(self):
        pass

    def test(self, char: str) -> bool:
        try:
            int(char)
            return True
        except ValueError:
            return False

    def finalize(self):
        return True


class SixDigitValidator(IValidator):
    def __init__(self):
        self._count = 0

    def reset(self):
        self._count = 0

    def test(self, char: str) -> bool:
        self._count += 1
        return self._count < 7

    def finalize(self):
        return self._count


class NeverDecreaseValidator(IValidator):
    def __init__(self):
        self._last = -1

    def reset(self):
        self._last = -1

    def test(self, char: str) -> bool:
        i = int(char)
        if i < self._last:
            return False
        self._last = i
        return True

    def finalize(self):
        return True


class TwoAdjacentDigetsValidator(IValidator):
    def __init__(self):
        self._last = ""
        self._found = False

    def reset(self):
        self._last = ""
        self._found = False

    def test(self, char: str) -> bool:
        if char == self._last:
            self._found = True
        self._last = char
        return True

    def finalize(self):
        return self._found


def main(puzzle_range):
    validator = Validator()
    validator.add_validator(IntegerValidator())
    validator.add_validator(SixDigitValidator())
    validator.add_validator(NeverDecreaseValidator())
    validator.add_validator(TwoAdjacentDigetsValidator())

    bottom, top = puzzle_range.split("-")
    running_total = 0
    for pw in range(int(bottom), int(top)):
        if validator.test(str(pw)):
            running_total += 1
    print(f"Total possible passwords: {running_total}")


if __name__ == "__main__":
    main(argv[-1])
