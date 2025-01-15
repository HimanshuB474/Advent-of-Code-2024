from collections import deque
from typing import TypeAlias

TPos: TypeAlias = tuple[int, int]

# Read input from the file
with open("input.txt", "r") as file:
    rows = file.read().strip().split("\n")

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
CHEAT_LIMIT, THRESHOLD = 20, 100

grid = set()
spos, epos = None, None

# Parse the input to initialize the grid and start/end positions
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == "#":
            continue
        grid.add((i, j))
        if c == "S":
            spos = (i, j)
        if c == "E":
            epos = (i, j)

def traverse(grid: set[TPos], s: TPos) -> tuple[dict[TPos, int], dict[TPos, TPos]]:
    """Traverse the grid and calculate steps and paths."""
    Q, steps, last = deque([s]), {s: 0}, {}
    while Q:
        pos = Q.popleft()
        for d in DIRS:
            pos_ = pos[0] + d[0], pos[1] + d[1]
            if pos_ in steps or pos_ not in grid:
                continue
            steps[pos_] = steps[pos] + 1
            last[pos_] = pos
            Q.append(pos_)
    return steps, last

# Traverse the grid
picos, last = traverse(grid, spos)

# Trace back the path from end position to start position
pos_, path = epos, [epos]
while pos_ != spos:
    pos_ = last[pos_]
    path.append(pos_)

# Calculate answers based on the CHEAT_LIMIT and THRESHOLD
ans = ans2 = 0
for p1 in path:
    for i in range(-CHEAT_LIMIT, CHEAT_LIMIT + 1):
        for j in range(-1 * (CHEAT_LIMIT - abs(i)), CHEAT_LIMIT - abs(i) + 1):
            d = abs(i) + abs(j)
            if d == 0 or d > CHEAT_LIMIT:
                continue
            p2 = p1[0] + i, p1[1] + j
            if p2 not in grid:
                continue
            if picos[p2] - picos[p1] - d < THRESHOLD:
                continue
            ans += d == 2
            ans2 += 1

# Write output to files
with open("output1.txt", "w") as file:
    file.write(str(ans))

with open("output2.txt", "w") as file:
    file.write(str(ans2))
