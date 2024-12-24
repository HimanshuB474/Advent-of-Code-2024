# Open and read the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Initialize dictionaries for known values and formulas
known = {}
formulas = {}

# Parse the input for known values and formulas
parsing_known = True
for line in lines:
    line = line.strip()
    if not line:
        parsing_known = False
        continue
    if parsing_known:
        x, y = line.split(": ")
        known[x] = int(y)
    else:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

# Define the operators
operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
}

# Function to calculate wire values
def calc(wire):
    if wire in known:
        return known[wire]
    op, x, y = formulas[wire]
    # Use memoization for computed values
    known[wire] = operators[op](calc(x), calc(y))
    return known[wire]

# Compute the binary value for keys z00, z01, ...
z = []
i = 0
while True:
    key = f"z{i:02}"  # Generate key as z00, z01, ...
    if key not in formulas:
        break
    z.append(calc(key))
    i += 1

# Convert the binary result to an integer and print
print(int("".join(map(str, z[::-1])), 2))
