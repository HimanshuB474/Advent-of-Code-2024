import re

total = 0

# Read input from the file
with open("input.txt", "r") as file:
    data = file.read()

for block in data.split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    px += 10000000000000
    py += 10000000000000
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
    if ca % 1 == cb % 1 == 0:
        total += int(ca * 3 + cb)

# Write output to a file
with open("output.txt", "w") as file:
    file.write(str(total))
