"""
 
Intcode programs are given as a list of integers; these values are used as the initial state for the computer's memory.
When you run an Intcode program, make sure to
 
start by initializing memory to the program's values.
 
A position in memory is called an address
(for example, the first value in memory is at "address 0").
 
Opcodes (like 1, 2, or 99) mark the beginning of an instruction.
The values used immediately after an opcode, if any, are called the instruction's parameters.
For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters.
The instruction 99 contains only an opcode and has no parameters.
 
The address of the current instruction is called the instruction pointer;
it starts at 0.
After an instruction finishes, the instruction pointer increases by the number of values in the instruction;
until you add more instructions to the computer,
this is always 4
(1 opcode + 3 parameters) for the add and multiply instructions.
(The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)
 
INPUTS
The inputs should still be provided to the program by replacing the values at addresses 1 and 2,
the value placed in address 1 is called the noun,
the value placed in address 2 is called the verb.
Each of the two input values will be between 0 and 99, inclusive.
 
Once the program has halted, its output is available at address 0,
 
Each time you try a pair of inputs, make sure you first reset the computer's memory to your puzzle input)
 
Find the input noun and verb that cause the program to produce the output 19690720.
 
"""
 
 
data = []
desired_ouput = 19690720
output = []
data_init = []
 
def set_opcode(op1: list):
    # print(op1)
    value_1_position = op1[1]
    value_2_position = op1[2]
    result_position = op1[3]
    global data
    global output
 
    if op1[0] == 1:
        data[result_position] = int(data[value_1_position]) + int(data[value_2_position])
        # print(f"set op1 {op1}: {int(data[value_1_position]) + int(data[value_2_position])}: {data[result_position]}")
    if op1[0] == 2:
        try:
            data[result_position] = int(data[value_1_position]) * int(data[value_2_position])
            # print(f"set op1 {op1}: {int(data[value_1_position]) * int(data[value_2_position])}: {data[result_position]}")
        except IndexError as e:
            # print(e,op1)
            pass
    if op1[0] > 2:
        # print(f"\nerror {op1}\n")
        # print(f"{data}")
        # quit()
        # print(data)
        pass

def process_data():
    global data
    global output
    output = data
    temp_opcode = []
 
    for i in range(len(data)):
       if len(temp_opcode) == 4:
           # print(f"length is 4")
           set_opcode(temp_opcode)
           temp_opcode.clear()
           temp_opcode.append(int(data[i]))
       else:
           temp_opcode.append(int(data[i]))
           # print(f"added to temp code {temp_opcode}")
 
def set_data(new_data: list):
   global data
   data = new_data
 
def update_data(position: int, value: int):
   global data
   data[position] = value

def reset_data():
    global data
    data = data_init
 
def get_data_from_file():
    global data_init
    with open('sample_resource.txt', 'r') as input_data:
       set_data(input_data.read().split(","))
       data_init = input_data.read().split(",")
 
 
def brute():
   global data
   pos_1 = 0 # noun
   pos_2 = 0 # verb
 
   for pos_1_guess in range(0, 100):
       for pos_2_guess in range(0 ,100):
           get_data_from_file() # OMG this was in the loop above - caused the issue :)
           data[1] = pos_1_guess
           data[2] = pos_2_guess
           print(f"pos 1: {pos_1_guess} pos 2: {pos_2_guess}")
           process_data()
           if data[0] == desired_ouput:
               print(f"Found match with {pos_1_guess} and {pos_2_guess} answer is {100 * pos_1_guess + pos_2_guess}")
               quit()
           else:
            # print(f"value {data[0]} {pos_1_guess} and {pos_2_guess}")
                print(f"value {data[0]},{data[1]},{data[2]},{data[3]}")
                #  get_data_from_file()
                reset_data()
       get_data_from_file()
 
get_data_from_file()
# process_data()
 
# print(f"{data[0]}")
brute()
