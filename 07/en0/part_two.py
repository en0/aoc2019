from sys import argv
from math import floor


class Intcode:
    def __init__(self, source: str):
        self._source = source
        self._initial_state = []
        self._state = []
        self._pc = 0
        self._hlt = True
        self._wait = False
        self._mode_pipeline = []
        self._opcodes = {
            1: add,
            2: mul,
            3: inp,
            4: outp,
            5: jnz,
            6: jz,
            7: lt,
            8: eq,
            99: hlt,
        }

    def _decode_instruction(self, instruction):
        opcode = instruction % 100
        modes = floor(instruction / 100)
        return opcode, modes

    def _set_mode_pipeline(self, modes: int):
        self._mode_pipeline = []
        while modes > 0:
            flag = modes % 10
            modes = floor(modes/10)
            self._mode_pipeline.append(flag)
        #print("PIPELINE: ", self._mode_pipeline)

    def _get_mode(self):
        try:
            return self._mode_pipeline.pop(0)
        except IndexError:
            return 0

    def install_opcode(self, code, hanlder):
        self._opcodes[code] = hanlder

    def load(self):
        with open(self._source, 'r') as fd:
            self._initial_state = [_ for _ in map(int, fd.read().split(","))]
        self.reset()

    def reset(self):
        self._pc = 0
        self._hlt = False
        self._wait = False
        self._state = [_ for _ in self._initial_state]

    def fetch_raw(self):
        self._pc += 1
        return self._state[self._pc - 1]

    def fetch(self):
        if self._get_mode() == 1:
            return self.fetch_raw()
        else:
            return self._state[self.fetch_raw()]

    def fetch_instruction(self):
        return self._decode_instruction(self.fetch_raw())

    def get(self, offset: int) -> int:
        return self._state[offset]

    def set(self, offset: int, value: int):
        while len(self._state) <= offset:
            self._state.append(0)
        self._state[offset] = value

    def jump(self, pc: int):
        self._pc = pc

    def hlt(self):
        print("HALT IS SET!!!!")
        self._hlt = True

    def wait(self):
        self._wait = True

    def is_hlt(self):
        return self._hlt

    def step(self):
        try:
            opcode, modes = self.fetch_instruction()
            handler = self._opcodes.get(opcode)
            if handler is None:
                raise Exception(f"Unknown Opcode: {opcode}")
            self._set_mode_pipeline(modes)
            handler(self)
        except Exception as ex:
            self.core_dump(self._pc - 1)
            raise ex

    def run(self):
        while not self._hlt:
            self.step()
            if self._wait:
                return

    def resume(self):
        self._wait = False
        self.run()

    def resume_debug(self):
        self._wait = False
        self.debug()

    def debug(self):
        while not self._hlt:
            self.core_dump()
            input("...")
            self.step()
            if self._wait:
                return

    def core_dump(self, pc=None):
        pc = pc or self._pc
        low = max(0, pc - 5)
        high = min(len(self._state), pc + 15)
        opcode, mode = self._decode_instruction(self._state[pc])
        handler = self._opcodes.get(opcode)
        fn_name = handler.__name__ if handler is not None else "UNKNOWN"
        print("*" * 20)
        print(f"PC:{pc:001}  HLT:{self._hlt}")
        print(f"OPC:{opcode} MOD:{mode}")
        print("-" * 20)
        for i in range(low, high):
            if i == pc:
                print(f"{i}:----> {self._state[i]} [{fn_name}]")
            else:
                print(f"{i}:      {self._state[i]}")
        print("*" * 20)


class Amplifier:
    def __init__(self, prog: str, name):
        self.name = name
        self._controller = Intcode(prog)
        self._inputs = []
        self._outputs = []

    def initialize(self):
        self._controller.load()
        self._controller.install_opcode(3, self._controller_read) # Input
        self._controller.install_opcode(4, self._controller_write) # Output

    def reset(self):
        self._inputs = []
        self._outputs = []
        self._controller.reset()

    def push_value(self, value: int):
        self._inputs.append(value)

    def pop_value(self):
        try:
            return self._outputs.pop(0)
        except IndexError:
            return None

    def run_cycle(self):
        self._controller.resume()
        return not self._controller.is_hlt()

    def is_hlt(self):
        return self._controller.is_hlt()

    def _controller_read(self, p: Intcode):
        a = p.fetch_raw()
        v = self._inputs.pop(0)
        p.set(a, v)

    def _controller_write(self, p: Intcode):
        v = p.fetch()
        self._outputs.append(v)
        p.wait()
        

class ThrusterController:
    def __init__(self, prog: str):
        self._v = 0
        self._amps = [
            Amplifier(prog, "A"),
            Amplifier(prog, "B"),
            Amplifier(prog, "C"),
            Amplifier(prog, "D"),
            Amplifier(prog, "E"),
        ]

    def initialize(self):
        [a.initialize() for a in self._amps]

    def run(self, phase: list):
        print(phase)
        for amp, p in zip(self._amps, phase):
            amp.reset()
            amp.push_value(p)

        v = 0
        last_val_by_amp = dict()
        running = True
        while running:
            for amp in self._amps:
                amp.push_value(v)
                if not amp.run_cycle():
                    print("HTL: ", amp.name, last_val_by_amp['E'])
                    return last_val_by_amp['E']
                print("WAIT: ", amp.name, v)
                v = amp.pop_value()
                last_val_by_amp[amp.name] = v
        return -1


def add(p: Intcode):
    a = p.fetch()
    b = p.fetch()
    c = p.fetch_raw()
    val = a + b
    p.set(c, val)


def mul(p: Intcode):
    a = p.fetch()
    b = p.fetch()
    c = p.fetch_raw()
    val = a * b
    p.set(c, val)


def hlt(p: Intcode):
    p.hlt()


def lt(p: Intcode):
    """Less than.

    If the first parameter less than the second,
    store 1 in the position pointed to by the 3rd.
    Otherwise store zero in the position pointed to
    by the 3rd.
    """
    a = p.fetch()
    b = p.fetch()
    o = p.fetch_raw()
    p.set(o, 1 if a < b else 0)


def eq(p: Intcode):
    """Equal to.

    If the first parameter is equal to the second,
    store 1 in the position pointed to by the 3rd.
    Otherwise store zero in the position pointed to
    by the 3rd.
    """
    a = p.fetch()
    b = p.fetch()
    o = p.fetch_raw()
    p.set(o, 1 if a == b else 0)


def jnz(p: Intcode):
    """Jump if true.

    If the first parameter is non-zero,
    set PC to the value of the second parameter.
    """
    a = p.fetch()
    pc = p.fetch()
    if a != 0:
        p.jump(pc)


def jz(p: Intcode):
    """Jump if false.

    If the first parameter is zero,
    set PC to the value of the second parameter.
    """
    a = p.fetch()
    pc = p.fetch()
    if a == 0:
        p.jump(pc)


def inp(p: Intcode):
    v = input("INPUT: ")
    a = p.fetch_raw()
    p.set(a, int(v))


def outp(p: Intcode):
    v = p.fetch()
    print(f"OUTPUT: {v}")


def main(resource_path):
    t = ThrusterController(resource_path)
    t.initialize()
    m = -1
    p = None
    # Really? Ian? Really!!?
    for a in range(5, 10):
        for b in [_ for _ in range(5, 10) if _ not in [a]]:
            for c in [_ for _ in range(5, 10) if _ not in [a,b]]:
                for d in [_ for _ in range(5, 10) if _ not in [a,b,c]]:
                    for e in [_ for _ in range(5, 10) if _ not in [a,b,c,d]]:
                        v = t.run([a,b,c,d,e])
                        if v > m:
                            m = v
                            p = [a,b,c,d,e]
    print(m, p)



if __name__ == "__main__":
    main(argv[-1])
