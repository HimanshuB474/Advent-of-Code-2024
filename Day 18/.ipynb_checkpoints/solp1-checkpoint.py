from collections import deque

s = 70
n = 1024

# Initialize the grid and populate obstacle coordinates
grid = [[0] * (s + 1) for _ in range(s + 1)]
with open("input.txt") as f:
    coords = [tuple(map(int, line.split(","))) for line in f]

for c, r in coords[:n]:
    grid[r][c] = 1

# BFS initialization
q = deque([(0, 0, 0)])  # (row, column, distance)
seen = set([(0, 0)])  # Avoid duplicate visits

# BFS loop
while q:
    r, c, d = q.popleft()
    for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
        # Ensure within bounds and not revisiting cells or hitting obstacles
        if 0 <= nr <= s and 0 <= nc <= s and (nr, nc) not in seen and grid[nr][nc] == 0:
            if nr == s and nc == s:  # Found the target
                print(d + 1)
                exit(0)
            seen.add((nr, nc))
            q.append((nr, nc, d + 1))
