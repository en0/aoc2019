'''
read file
split data on line return file_line1 file_line2
split data on comma for both lines
iterate through each instruction for each line to create wire1 wire2
if points go from (0,0) to (0,3) line = (0,0),(0,1),(0,2),(0,3)
if r,l,u,d add number

'''

class TraceCircuit():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._cords = []
        self._steps = []
        self._file_line_1 = []
        self._file_line_2 = []
        self._file_data = []
        self._get_data_from_file()
        self._set_cords()

    def _up(self, count: str):
        # print(f"{self._y} added to {count} is {self._y + int(count)}")
        # self._y += int(count)
        self.lines_from_instruction("y", int(count))
        # self._set_cords()

    def _down(self, count: str):
        # print(f"{self._y} subtract {count} is {self._y - int(count)}")
        self.lines_from_instruction("y", int(count))
        # self._y -= int(count)
        # self._set_cords()

    def _left(self, count: str):
        # print(f"{self._x} subtract {count} is {self._x - int(count)}")
        self.lines_from_instruction("x", int(count))
        # self._x -= int(count)
        # self._set_cords()

    def _right(self, count: str):
        # print(f"{self._x} added to {count} is {self._x + int(count)}")
        self.lines_from_instruction("x", int(count))
        # self._x += int(count)
        # self._set_cords()

    def _get_data_from_file(self):
        lines = []
        file_count = 0
        with open('sample2.txt', 'r') as input_data:
            parts = input_data.read().split("\n")
            self._file_line_1 = parts[0].split(",")
            self._file_data.append(self._file_line_1)
            self._file_line_2 = parts[1].split(",")
            self._file_data.append(self._file_line_2)

    def _set_cords(self):
        self._cords.append({"x": self._x, "y": self._y})
        print({"x": self._x, "y": self._y})

    def _process_intcode(self, instruction: list):
        for step in instruction:
            count = int(step[1:])
            print(f"{step} : ")
            if step.startswith("U"):
                # self._up(step[1:])
                self.lines_from_instruction("y", int(count))
            if step.startswith("D"):
                # self._down(step[1:])
                self.lines_from_instruction("y", int(count * -1))
            if step.startswith("L"):
                # self._left(step[1:])
                self.lines_from_instruction("x", int(count * -1))
            if step.startswith("R"):
                # self._right(step[1:])
                self.lines_from_instruction("x", int(count))
            # self._set_cords()
            # print(f"{step}: {self._cords}\n\n")

    def lines_from_instruction(self, x_or_y: str, end_point: int):
        line_parts = []
        print(end_point)
        for _ in range(end_point):
            print(f"{_} : {end_point}: {x_or_y}")
            if x_or_y == 'x':
                # line_parts.append[x_or_y,self._y]
                self._y = _
                self._set_cords()
            else:
                self._x = _
                self._set_cords()

    def get_list_of_points(self):
        point_set = []
        # print(self._file_line_1 == self._file_line_2)
        for instruction in self._file_data:
            # print("start")
            self._process_intcode(instruction)
            point_set.append(self._cords)
            self._cords = [{"x": 0, "y": 0}]
            self._x = 0
            self._y = 0
        # print(point_set[0] == point_set[1])
            # self._process_intcode(self._file_line_1)
            # point_set.append(self._cords)
            # self._cords = [{"x": 0, "y": 0}]
            # self._process_intcode(self._file_line_2)
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
# print(len(cord_set[1]))

point_index = 0
best_match = 0

# for points1 in cord_set[0]:
    # print(points1)
    # for points2 in cord_set[1]:
        # print(f"{points1} : {points2}")
        # print(f"{points1['x']},{points1['y']},{points2['x']},{points2['y']},")
        # print(f"{points1 == points2} : {points1['x']} and {points2['x']} ")
        # if points1 == points2:
        #     # print(f"match {points1} : {points2}")
        #     dist1 = test.calc_mahatten( [points1['x'], points1['y']])
        #     dist2 = test.calc_mahatten( [points2['x'], points2['y']])
        #     if dist1 < dist2:
        #         if dist1 < best_match:
        #             best_match = dist1
        #     else:
        #         if dist2 < best_match:
        #             best_match = dist2
    # point_index += 1
print(best_match)

