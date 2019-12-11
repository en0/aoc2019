class TraceCircuit():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._cords = []
        self._steps = []
        self._wire_1 = []
        self._wire_2 = []
        self._wires = []
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
            self._wires.append(self._wire_1)
            self._wire_2 = parts[1].split(",")
            self._wires.append(self._wire_2)

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
        print(self._wire_1 == self._wire_2)
        for wire in self._wires:

            self._process_intcode(wire)
            point_set.append(self._cords)
        self._cords = [{"x": 0, "y": 0}]
        self._x = 0
        self._y = 0
        # print(point_set[0] == point_set[1])
            # self._process_intcode(self._wire_1)
            # point_set.append(self._cords)
            # self._cords = [{"x": 0, "y": 0}]
            # self._process_intcode(self._wire_2)
            # point_set.append(self._cords)
        return point_set

    def calc_mahatten(self, input_cord: list):
        # abs(x1-x2)+(y1-y2)
        # x1 = input_cord[0]['x']
        x1 = 0
        x2 = input_cord[1]['x']
        # y1 = input_cord[0]['y']
        y1 = 0
        y2 = input_cord[1]['y']
        # print(input_cord)

        distance = abs(x1 - x2) + abs(y1 -y2)
        return distance


test = TraceCircuit()
cord_set = test.get_list_of_points()
# print(cord_set[0] == cord_set[1])
# point_index = 0
# for points1 in cord_set[0]:
#     for points2 in cord_set[1]:
#         # if points1 == cord_set[1][point_index]:
#         print(f"points { points1} and {points2}")
#     point_index += 1
