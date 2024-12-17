from collections import deque

# Read the input grid from the file "input.txt"
with open("input.txt") as f:
    grid = [[int(char) for char in line.strip()] for line in f]

rows, cols = len(grid), len(grid[0])

# Identify all trailheads (cells with value 0)
trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

def score(grid, r, c):
    q = deque([(r, c)])
    seen = {(r, c): 1}
    trails = 0
    while len(q) > 0:
        cr, cc = q.popleft()
        if grid[cr][cc] == 9:
            trails += seen[(cr, cc)]
        for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
            if grid[nr][nc] != grid[cr][cc] + 1: continue
            if (nr, nc) in seen:
                seen[(nr, nc)] += seen[(cr, cc)]
                continue
            seen[(nr, nc)] = seen[(cr, cc)]
            q.append((nr, nc))
    return trails

# Calculate the total number of trails from all trailheads
result = sum(score(grid, r, c) for r, c in trailheads)
print(result)
