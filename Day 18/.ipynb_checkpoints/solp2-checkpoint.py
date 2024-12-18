from collections import deque

s = 70

# Read and process input coordinates
with open("input.txt") as f:
    coords = [tuple(map(int, line.split(","))) for line in f]

def connected(n):
    # Initialize the grid and populate obstacle coordinates
    grid = [[0] * (s + 1) for _ in range(s + 1)]
    for c, r in coords[:n]:
        grid[r][c] = 1

    # BFS setup
    q = deque([(0, 0)])
    seen = {(0, 0)}

    # BFS loop
    while q:
        r, c = q.popleft()
        for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            # Ensure valid move
            if 0 <= nr <= s and 0 <= nc <= s and grid[nr][nc] == 0 and (nr, nc) not in seen:
                if nr == s and nc == s:  # Target found
                    return True
                seen.add((nr, nc))
                q.append((nr, nc))

    return False

# Binary search to find the minimum index where connectivity is lost
lo, hi = 0, len(coords) - 1

while lo < hi:
    mi = (lo + hi) // 2
    if connected(mi + 1):
        lo = mi + 1  # Explore the upper half
    else:
        hi = mi  # Explore the lower half

# Output the problematic coordinate
print(*coords[lo], sep=",")
