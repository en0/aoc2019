class TraceCircuit():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._cords = []
        self._steps = []
        self._wire_1 = []
        self._wire_2 = []
        self._get_data_from_file()
        self._set_cords()

    def _up(self, count: str):
        self._y += int(count)
        self._set_cords()

    def _down(self, count: str):
        self._y -= int(count)
        self._set_cords()

    def _left(self, count: str):
        self._x -= int(count)
        self._set_cords()

    def _right(self, count: str):
        self._x += int(count)
        self._set_cords()

    def _get_data_from_file(self):
        lines = []
        file_count = 0
        with open('sample.txt', 'r') as input_data:
            parts = input_data.read().split("\n")
            self._wire_1 = parts[0].split(",")
            self._wire_2 = parts[1].split(",")

    def _set_cords(self):
        self._cords.append({"x": self._x, "y": self._y})

    def _process_intcode(self, instruction: list):
        count = 0
        for step in instruction:
            if step.startswith("U"):
                self._up(step[1:])
            if step.startswith("D"):
                self._down(step[1:])
            if step.startswith("L"):
                self._left(step[1:])
            if step.startswith("R"):
                self._right(step[1:])
            # self._set_cords()
            # print(f"{step}: {self._cords}\n\n")

    def get_list_of_points(self):
        point_set = []
        self._process_intcode(self._wire_1)
        point_set.append(self._cords)
        self._cords = [{"x": 0, "y": 0}]
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
        # print(cord_set)

        distance = abs(x1 - x2) + abs(y1 -y2)
        return distance


test = TraceCircuit()
# test.process_intcode(test._wire_1)
cord_set = test.get_list_of_points()

# print(point_set)
# point_index = 0
# for point in point_set[0]:
    # print(f"{point}...{point_set[1][point_index]}\n")
    # point_index += 1

# print(cord_set[0]==cord_set[1])
# print(f"{point_set[0]}\n{point_set[1]}\n")
# print(f"{point_set[0]['x']} {points[1]['x']}")

point_index = 0
for points1 in cord_set[0]:
    # for points2 in cord_set[1]:
    if points1 == cord_set[1][point_index]:
        print(f"points { points1} and {cord_set[1][point_index]}")
    point_index += 1
# points_index = 0
# manhatten_results = []
# def x2_is_same(x1):
#     for points2 in point_set[1]:
#         if x1 == points2:
#             print(f"match {x1} and {points2}")

# for points in point_set[0]:
#     x1 = points['x']
#     if x2_is_same(points):
#         # print(x1)
#         pass
#     for _ in points:
#         matches = []
#         x1 = points[points_index]
#         x2 = _

#         if x1 == x2:
#             print(f"{x1} and {x2}")
#             result = test.calc_mahatten([x1,x2])
#             manhatten_results.append({
#                 "x1": x1,
#                 "x2": x2,
#                 "result": result
#             })
#             # print(f"match{_}")
#             pass
#         else:
#             # print(f"no match {x1} and {x2}")
#         # print(points[0]['x'])
#             pass
#     points_index += 1

# print(manhatten_results)

# print(test._cords)
# test.get_data_from_file()