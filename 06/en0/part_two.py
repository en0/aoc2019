from sys import argv
from part_one import Map, Node
from itertools import zip_longest


class Map2(Map):
    def find_route(self, src: Node, dest: Node):
        """Find the sortest route between the 2 given nodes.

        Because this an undirected asyclic graph, there is only 1
        route route between 2 points. I will find the path from
        root to src and dest and use the least common ancestor to
        remove the part of the path that is not between src and
        dest.
        """
        orig_to_source = reversed(self.path_to_origin(src))
        orig_to_dest = reversed(self.path_to_origin(dest))
        s_half = list()
        d_half = list()
        for s, d in zip_longest(orig_to_source, orig_to_dest):
            if s is d:
                continue
            if s is not None:
                s_half.append(s)
            if d is not None:
                d_half.append(d)

        return s_half + d_half

    def path_to_origin(self, node: Node):
        """Find the route from the given node to the origin

        Since there is only one route to origin, just follow the 
        parent chain all the way to root.
        """
        route = list()
        while node.parent is not None:
            route.append(node.parent)
            node = node.parent
        return route

def main(resource_path):
    catalog = Map2.load(resource_path)
    you = catalog.get_node("YOU")
    san = catalog.get_node("SAN")
    print(len(catalog.find_route(you, san)))

if __name__ == "__main__":
    main(argv[-1])
