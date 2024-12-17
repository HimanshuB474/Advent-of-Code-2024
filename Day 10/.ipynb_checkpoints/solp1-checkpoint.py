from collections import deque

# Read the input grid from the file "input.txt"
with open("input.txt") as f:
    grid = [[int(char) for char in line.strip()] for line in f]

rows, cols = len(grid), len(grid[0])

# Identify all trailheads (cells with value 0)
trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

def score(grid, r, c):
    q = deque([(r, c)])
    seen = set([(r, c)])
    summits = 0

    while q:
        cr, cc = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # Four directions
            nr, nc = cr + dr, cc + dc
            # Check boundaries and valid next step
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == grid[cr][cc] + 1:
                seen.add((nr, nc))
                if grid[nr][nc] == 9:
                    summits += 1
                else:
                    q.append((nr, nc))
    return summits

# Calculate the total number of summits from all trailheads
result = sum(score(grid, r, c) for r, c in trailheads)
print(result)
