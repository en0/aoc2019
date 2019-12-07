from sys import argv
from math import floor


class Node:
    def __init__(self, name: str):
        self.value = 0
        self.children = list()
        self.parent = None
        self.name = name

    def orbited_by(self, node: "Node"):
        node.set_parent(self)
        self.children.append(node)

    def set_parent(self, parent: "Node"):
        self.value = parent.value + 1
        self.parent = parent
        for c in self.children:
            c.set_parent(self)

    def __repr__(self):
        return f"<Node name={self.name}, value={self.value}>"


class Map:
    def __init__(self):
        self._cache = dict()
        self._root = None

    def get_node(self, name) -> Node:
        if name not in self._cache:
            self._cache[name] = Node(name)
            if name == "COM" and self._root is None:
                self._root = self._cache[name]
        return self._cache[name]

    def checksum(self) -> int:
        assert(self._root is not None)
        return sum([n.value for n in self._cache.values()])

    @classmethod
    def load(cls, map_path: str):
        catalog = cls()
        with open(map_path, 'r') as fd:
            for line in fd:
                line = line.rstrip("\n")
                l, r = line.split(")")
                node_l = catalog.get_node(l)
                node_r = catalog.get_node(r)
                node_l.orbited_by(node_r)
        return catalog


def main(resource_path):
    catalog = Map.load(resource_path)
    print(catalog.checksum())

if __name__ == "__main__":
    main(argv[-1])
