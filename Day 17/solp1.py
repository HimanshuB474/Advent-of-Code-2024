def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract register values
    registers = [0, 0, 0]
    for line in lines:
        if line.startswith("Register A"):
            registers[0] = int(line.split(":")[1].strip())
        elif line.startswith("Register B"):
            registers[1] = int(line.split(":")[1].strip())
        elif line.startswith("Register C"):
            registers[2] = int(line.split(":")[1].strip())

    # Extract program
    program = []
    for line in lines:
        if line.startswith("Program"):
            program = list(map(int, line.split(":")[1].strip().split(",")))

    return registers, program

def run_program(registers, program):
    # Initialize registers and instruction pointer
    A, B, C = registers
    ip = 0  # instruction pointer
    output = []

    # Helper function for combo operands
    def get_combo_value(operand):
        if operand in [0, 1, 2, 3]:  # Literal values
            return operand
        elif operand == 4:  # Register A
            return A
        elif operand == 5:  # Register B
            return B
        elif operand == 6:  # Register C
            return C
        else:
            raise ValueError("Invalid combo operand")

    # Main loop to run the program
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2  # Move to the next instruction unless overridden

        if opcode == 0:  # adv
            A //= 2 ** get_combo_value(operand)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            B = A // (2 ** get_combo_value(operand))
        elif opcode == 7:  # cdv
            C = A // (2 ** get_combo_value(operand))
        else:
            raise ValueError("Invalid opcode")

    # Join outputs with commas and return
    return ",".join(map(str, output))

# File path
input_file = "input.txt"

# Read input and run the program
registers, program = read_input(input_file)
result = run_program(registers, program)
print("Output:", result)
