import re

# Read input efficiently from the file "input.txt"
with open("input.txt") as file:
    program = list(map(int, re.findall(r"\d+", file.read())[3:]))

# Ensure the program ends with JNZ 0
assert program[-2:] == [3, 0], "program does not end with JNZ 0"

# Function to recursively find the solution
def find(target, ans):
    if not target:
        return ans  # If target list is empty, return the answer

    for t in range(8):  # Loop through 0 to 7
        a = (ans << 3) | t  # Combine previous answer with t
        b, c = 0, 0  # Reset b and c
        output = None
        adv3 = False

        # Helper function to handle combo operands
        def combo(operand):
            if 0 <= operand <= 3:
                return operand
            if operand == 4:
                return a
            if operand == 5:
                return b
            if operand == 6:
                return c
            raise AssertionError(f"unrecognized combo operand {operand}")

        # Process instructions in the program
        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]

            if ins == 0:  # ADV instruction
                assert not adv3, "program has multiple ADVs"
                assert operand == 3, "program has ADV with operand other than 3"
                adv3 = True
            elif ins == 1:  # XOR instruction
                b ^= operand
            elif ins == 2:  # MOD 8 instruction
                b = combo(operand) % 8
            elif ins == 3:  # Invalid JNZ in body
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:  # XOR with c
                b ^= c
            elif ins == 5:  # Output instruction
                assert output is None, "program has multiple OUT"
                output = combo(operand) % 8
            elif ins == 6:  # Right shift instruction for b
                b = a >> combo(operand)
            elif ins == 7:  # Right shift instruction for c
                c = a >> combo(operand)

            # If output matches the last target, recursively call find
            if output == target[-1]:
                sub = find(target[:-1], a)
                if sub is not None:
                    return sub

    return None  # Return None if no solution found

# Run the function with the program input and print the result
print(find(program, 0))
