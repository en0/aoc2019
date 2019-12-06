from sys import argv
from part_one import Intcode

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

def main(resource_path):
    ic = Intcode(resource_path)
    ic.install_opcode(5, jnz)
    ic.install_opcode(6, jz)
    ic.install_opcode(7, lt)
    ic.install_opcode(8, eq)
    ic.load()

    #ic.debug()
    ic.run()


if __name__ == "__main__":
    main(argv[-1])
