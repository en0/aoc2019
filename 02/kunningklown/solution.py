data = []

def set_opcode(op1: list):
    value_1_position = op1[1]
    value_2_position = op1[2]
    result_position = op1[3]
    global data
    global output

    if op1[0] == 1:
        data[result_position] = int(data[value_1_position]) + int(data[value_2_position])
        print(f"set op1 {op1}: {int(data[value_1_position]) + int(data[value_2_position])}: {data[result_position]}")
    if op1[0] == 2:
        data[result_position] = int(data[value_1_position]) * int(data[value_2_position])
        print(f"set op1 {op1}: {int(data[value_1_position]) * int(data[value_2_position])}: {data[result_position]}")
    if op1[0] > 2:
        print(f"\nerror {op1}\n")
        print(f"{data}")
        quit()


def process_data():
    global data
    global output
    output = data
    temp_opcode = []

    for i in range(len(data)):
        if len(temp_opcode) == 4:
            print(f"length is 4")
            set_opcode(temp_opcode)
            temp_opcode.clear()
            temp_opcode.append(int(data[i]))
        else:
            temp_opcode.append(int(data[i]))
            print(f"added to temp code {temp_opcode}")


def get_data_from_file():
    global data
    with open('sample_resource.txt', 'r') as input_data:
        data = input_data.read()
    data = data.split(",")


get_data_from_file()
process_data()
print(f"{data}")
