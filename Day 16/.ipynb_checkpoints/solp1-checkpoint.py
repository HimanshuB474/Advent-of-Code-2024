import heapq

# Read and prepare the grid
grid = [list(line.strip()) for line in open("input.txt")]

rows, cols = len(grid), len(grid[0])

# Find the starting position 'S'
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            sr, sc = r, c
            break
    else:
        continue
    break

# Priority queue and seen set initialization
pq = [(0, sr, sc, 0, 1)]  # (cost, row, col, direction_row, direction_col)
seen = set([(sr, sc, 0, 1)])

def is_within_bounds(nr, nc):
    return 0 <= nr < rows and 0 <= nc < cols

# Pathfinding loop
while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)

    # Check if we reached the end position 'E'
    if grid[r][c] == "E":
        print(cost)
        break

    # Generate possible moves
    for new_cost, nr, nc, ndr, ndc in [
        (cost + 1, r + dr, c + dc, dr, dc),
        (cost + 1000, r, c, dc, -dr),
        (cost + 1000, r, c, -dc, dr)
    ]:
        # Validate next position and state
        if is_within_bounds(nr, nc) and grid[nr][nc] != "#" and (nr, nc, ndr, ndc) not in seen:
            seen.add((nr, nc, ndr, ndc))  # Mark as seen
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))
