class TraceCircuit():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._cords = []
        self._steps = []
        self._wire_1 = []
        self._wire_2 = []
        self._get_data_from_file()
        self._grid = {
            "a": [range(1,12)],
            "b": [range(1,12)],
            "c": [range(1,12)],
            "d": [range(1,12)],
            "e": [range(1,12)],
            "f": [range(1,12)],
            "g": [range(1,12)],
            "h": [range(1,12)],
            "i": [range(1,12)],
            "j": [range(1,12)],
            "k": [range(1,12)]
        }

    # grid_11_x_10 = [
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0,0]
    # ]

    # grid = {
    #     "a": [0,0,0,0,0,0,0,0,0,0,0],
    #     "b": [0,0,0,0,0,0,0,0,0,0,0],
    #     "c": [0,0,0,0,0,0,0,0,0,0,0],
    #     "d": [0,0,0,0,0,0,0,0,0,0,0],
    #     "e": [0,0,0,0,0,0,0,0,0,0,0],
    #     "f": [0,0,0,0,0,0,0,0,0,0,0],
    #     "g": [0,0,0,0,0,0,0,0,0,0,0],
    #     "h": [0,0,0,0,0,0,0,0,0,0,0],
    #     "i": [0,0,0,0,0,0,0,0,0,0,0],
    #     "j": [0,0,0,0,0,0,0,0,0,0,0],
    #     "k": [0,0,0,0,0,0,0,0,0,0,0]
    # }

    # grid
    # a   b   c   d   e   f   g   h   i   j
    # 1   1   1   1   1   1   1   1   1   1
    # 2   2   2   2   2   2   2   2   2   2
    # 3   3   3   3   3   3   3   3   3   3
    # 4   4   4   4   4   4   4   4   4   4
    # 5   5   5   5   5   5   5   5   5   5
    # 6   6   6   6   6   6   6   6   6   6
    # 7   7   7   7   7   7   7   7   7   7
    # 8   8   8   8   8   8   8   8   8   8
    # 9   9   9   9   9   9   9   9   9   9
    # 10  10  10  10  10  10  10  10  10  10
    # 11  11  11  11  11  11  11  11  11  11

    # grid = {
    #     "a": [range(1,12)],
    #     "b": [range(1,12)],
    #     "c": [range(1,12)],
    #     "d": [range(1,12)],
    #     "e": [range(1,12)],
    #     "f": [range(1,12)],
    #     "g": [range(1,12)],
    #     "h": [range(1,12)],
    #     "i": [range(1,12)],
    #     "j": [range(1,12)],
    #     "k": [range(1,12)]
    # }

    # grid_rows = [a,b,c,d,e,f,g,h,i,j] # number of top rows
    # grid_columns = [range(1, 12)] # number of columns 1,2,3,4,5,6,7,8,9,10,11
    # (abs(p1 - q1)+ abs(p2 - q2))

    def _up(self, count: str):
        self._y += int(count)
        # self._set_cords()

    def _down(self, count: str):
        self._y -= int(count)

    def _left(self, count: str):
        self._x -= int(count)

    def _right(self, count: str):
        # print(f"{self._x } + {count}")
        self._x += int(count)
        # print(f"is {self._x}")

    def _get_data_from_file(self):
        lines = []
        file_count = 0
        with open('sample.txt', 'r') as input_data:
            parts = input_data.read().split("\n")
            self._wire_1 = parts[0].split(",")
            self._wire_2 = parts[1].split(",")

    def _set_cords(self):
        # print(f"{[self._x, self._y]} {self._cords}")
        self._cords.append({"x": self._x, "y": self._y})
        # self._plot_points(self._cords)
        # print(f"{self._x, self._y} {self._cords}")

    # def get_wires(self):
    #     return [self._wire_1, self._wire_2]
    # def _plot_points(self, points: list):
    #     self._steps.append(points)

    def _process_intcode(self, instruction: list):
        for step in instruction:
            # print(f"{step} {self._cords}")
            if step.startswith("U"):
                self._up(step[1:])
                # self._set_cords
            if step.startswith("D"):
                self._down(step[1:])
            if step.startswith("L"):
                self._left(step[1:])
            if step.startswith("R"):
                self._right(step[1:])
            self._set_cords()
            # print(f"{step}\n {self._cords}\n\n")

    def get_list_of_points(self):
        point_set = []
        self._process_intcode(self._wire_1)
        point_set.append(self._cords)
        self._process_intcode(self._wire_2)
        point_set.append(self._cords)
        return point_set

    def calc_mahatten(self, cord_set: list):
        #abs(x1-x2)+(y1-y2)
        # x1 = cord_set[0]['x']
        x1 = 0
        x2 = cord_set[1]['x']
        # y1 = cord_set[0]['y']
        y1 = 0
        y2 = cord_set[1]['y']
        print(cord_set)

        distance = (x1 - x2) + (y1 -y2)
        return distance




test = TraceCircuit()
# test.process_intcode(test._wire_1)
point_set = test.get_list_of_points()
# print(test._cords)
# print(point_set)

points_index = 0
manhatten_results = []
for points in point_set:
    for _ in points:
        matches = []
        x1 = points[points_index]
        x2 = _

        if x1 == x2:
            print(f"{x1} and {x2}")
            result = test.calc_mahatten([x1,x2])
            manhatten_results.append({
                "x1": x1,
                "x2": x2,
                "result": result
            })
            # print(f"match{_}")
            pass
        else:
            # print(f"no match {x1} and {x2}")
        # print(points[0]['x'])
            pass
    points_index += 1
print(manhatten_results)

# print(test._cords)
# test.get_data_from_file()