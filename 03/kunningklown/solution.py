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
        # print(f"{self._y} added to {count} is {self._y + int(count)}")
        self._y += int(count)
        self._set_cords()

    def _down(self, count: str):
        # print(f"{self._y} subtract {count} is {self._y - int(count)}")
        self._y -= int(count)
        self._set_cords()

    def _left(self, count: str):
        # print(f"{self._x} subtract {count} is {self._x - int(count)}")
        self._x -= int(count)
        self._set_cords()

    def _right(self, count: str):
        # print(f"{self._x} added to {count} is {self._x + int(count)}")
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
        # print({"x": self._x, "y": self._y})

    def _process_intcode(self, instruction: list):
        count = 0
        for step in instruction:
            # print(step)
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
        # print(self._wire_1 == self._wire_2)
        for wire in self._wires:
            # print("start")
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
        x2 = input_cord[1]
        # y1 = input_cord[0]['y']
        y1 = 0
        y2 = input_cord[1]
        # print(input_cord)

        distance = abs(x1 - x2) + abs(y1 -y2)
        return distance


test = TraceCircuit()
cord_set = test.get_list_of_points()
# print(cord_set[0] == cord_set[1])
# print(f"x1,y1,x2,y2\n")
point_index = 0
for points1 in cord_set[0]:
    # print(point_index)
    for points2 in cord_set[1]:
        # print(f"{points1['x']},{points1['y']},{points2['x']},{points2['y']},")
        # print(f"{points1['x'] == points2['x']} : {points1['x']} and {points2['x']} ")
        if points1['x'] in range(points2['x']):
            print(f"match {points1} : {points2}")
            # x1_y1 =
            # point_a = test.calc_mahatten([points1['x'], points1['y']])
            # point_b = test.calc_mahatten([points2['x'], points2['y']])
            # if point_a > point_b:
            #     print(f"{point_a} is bigger than {point_b}")
            # else:
            #     print(f"{point_a} is smaller than {point_b}")
            # print(f"{point_index}: match {points1} and {cord_set[1][point_index]['x']}")
    point_index += 1

