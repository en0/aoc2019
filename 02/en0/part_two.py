from sys import argv
from part_one import Intcode


def main(resource_path):
    ic = Intcode(resource_path)
    ic.load()

    for i in range(0, 100):
        for j in range(0, 100):
            ic.reset()
            ic.set(1, i)
            ic.set(2, j)
            ic.run()
            if ic.get(0) == 19690720:
                print(100 * i + j)
                exit()

    print("No luck")

if __name__ == "__main__":
    main(argv[-1])
