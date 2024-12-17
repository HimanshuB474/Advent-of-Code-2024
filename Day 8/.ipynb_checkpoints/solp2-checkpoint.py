total = 0

def can_obtain(target, array, memo):
    # Use a memoization key based on current target and remaining array
    key = (target, len(array))
    if key in memo:
        return memo[key]

    if len(array) == 1:
        memo[key] = (target == array[0])
        return memo[key]

    if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1], memo):
        memo[key] = True
        return True

    if target > array[-1] and can_obtain(target - array[-1], array[:-1], memo):
        memo[key] = True
        return True

    s_target = str(target)
    s_last = str(array[-1])
    if s_target.endswith(s_last) and len(s_target) > len(s_last) and can_obtain(int(s_target[:-len(s_last)]), array[:-1], memo):
        memo[key] = True
        return True

    memo[key] = False
    return False

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if ": " not in line:
            continue

        l, r = line.split(": ")
        target = int(l)
        array = [int(x) for x in r.split()]
        
        # Pass a memoization dictionary
        if can_obtain(target, array, {}):
            total += target

grid = [line.strip() for line in open("input.txt") if line.strip()]

rows = len(grid)
cols = len(grid[0]) if grid else 0

antennas = {}

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != ".":
            if char not in antennas: antennas[char] = []
            antennas[char].append((r, c))

antinodes = set()

for array in antennas.values():
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j: continue
            r1, c1 = array[i]
            r2, c2 = array[j]
            dr = r2 - r1
            dc = c2 - c1
            r = r1
            c = c1
            while 0 <= r < rows and 0 <= c < cols:
                antinodes.add((r, c))
                r += dr
                c += dc

print(len(antinodes))
