from sys import argv


class Intcode:

    def __init__(self, source: str):
        self._source = source
        self._initial_state = []
        self._state = []
        self._pc = 0
        self._hlt = True
        self._opcodes = {
            1: add,
            2: mul,
            99: hlt,
        }

    def install_opcode(self, code, hanlder):
        self._opcodes[code] = hanlder

    def load(self):
        with open(self._source, 'r') as fd:
            self._initial_state = [_ for _ in map(int, fd.read().split(","))]
        self.reset()

    def reset(self):
        self._pc = 0
        self._hlt = False
        self._state = [_ for _ in self._initial_state]

    def fetch(self):
        self._pc += 1
        return self._state[self._pc - 1]

    def get(self, offset: int) -> int:
        return self._state[offset]

    def set(self, offset: int, value: int):
        self._state[offset] = value

    def jump(self, pc: int):
        self._pc = pc

    def hlt(self):
        self._hlt = True

    def step(self):
        self._opcodes.get(self.fetch())(self)

    def run(self):
        while not self._hlt:
            self.step()


def add(p: Intcode):
    a = p.fetch()
    b = p.fetch()
    c = p.fetch()
    val = p.get(a) + p.get(b)
    p.set(c, val)


def mul(p: Intcode):
    a = p.fetch()
    b = p.fetch()
    c = p.fetch()
    val = p.get(a) * p.get(b)
    p.set(c, val)


def hlt(p: Intcode):
    p.hlt()


def main(resource_path):
    ic = Intcode(resource_path)
    ic.load()

    # -- BEGIN PATCH --
    # restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it
    # had just before the last computer caught fire. To do this, before running the program, replace
    # position 1 with the value 12 and replace position 2 with the value 2
    ic.set(1, 12)
    ic.set(2, 2)
    # -- END PATCH --

    ic.run()
    print(ic.get(0))


if __name__ == "__main__":
    main(argv[-1])
