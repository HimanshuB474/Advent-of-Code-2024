# Open and read the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Parse the input
formulas = {}
parsing_known = True

for line in lines:
    line = line.strip()
    if not line:
        parsing_known = False
        continue
    if parsing_known:
        continue
    x, op, y, z = line.replace(" -> ", " ").split()
    formulas[z] = (op, x, y)

# Helper function to format wire names
def make_wire(char, num):
    return f"{char}{num:02}"

# Verification functions
def verify_z(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return (
        verify_intermediate_xor(x, num) and verify_carry_bit(y, num)
        or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
    )

def verify_intermediate_xor(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR":
        return False
    return (
        verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1)
        or verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)
    )

def verify_direct_carry(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return (
        verify_intermediate_xor(x, num) and verify_carry_bit(y, num)
        or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
    )

def verify(num):
    return verify_z(make_wire("z", num), num)

# Function to calculate progress
def progress():
    i = 0
    while verify(i):
        i += 1
    return i

# Find swaps to improve the baseline progress
swaps = []
for _ in range(4):
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y:
                continue
            # Swap formulas and check progress
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                swaps.extend([x, y])
                break
            # Revert the swap if no improvement
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break

# Output sorted swaps
print(",".join(sorted(swaps)))
