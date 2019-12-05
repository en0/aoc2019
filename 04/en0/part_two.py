from sys import argv

from part_one import (
    IValidator,
    Validator,
    IntegerValidator,
    SixDigitValidator,
    NeverDecreaseValidator)

class ImprovedTwoAdjacentDigetsValidator(IValidator):
    def __init__(self):
        self._last = ""
        self._ajacent_counts = {}

    def reset(self):
        self._last = ""
        self._adjacent_counts = {}

    def test(self, char: str) -> bool:
        self._adjacent_counts.setdefault(char, 1)
        if char == self._last:
            self._adjacent_counts[char] += 1
        self._last = char
        return True

    def finalize(self):
        return any([c == 2 for c in self._adjacent_counts.values()])

def main(puzzle_range):
    validator = Validator()
    validator.add_validator(IntegerValidator())
    validator.add_validator(SixDigitValidator())
    validator.add_validator(NeverDecreaseValidator())
    validator.add_validator(ImprovedTwoAdjacentDigetsValidator())

    bottom, top = puzzle_range.split("-")
    running_total = 0
    for pw in range(int(bottom), int(top)):
        if validator.test(str(pw)):
            running_total += 1
    print(f"Total possible passwords: {running_total}")


if __name__ == "__main__":
    main(argv[-1])
