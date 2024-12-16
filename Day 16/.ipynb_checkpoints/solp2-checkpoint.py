from collections import deque
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

# Priority queue and cost tracking initialization
pq = [(0, sr, sc, 0, 1)]  # (cost, row, col, direction_row, direction_col)
lowest_cost = {(sr, sc, 0, 1): 0}
backtrack = {}
best_cost = float("inf")
end_states = set()

# Pathfinding loop
while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
        continue
    if grid[r][c] == "E":
        if cost > best_cost:
            break
        best_cost = cost
        end_states.add((r, c, dr, dc))
    for new_cost, nr, nc, ndr, ndc in [
        (cost + 1, r + dr, c + dc, dr, dc),
        (cost + 1000, r, c, dc, -dr),
        (cost + 1000, r, c, -dc, dr)
    ]:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
            if new_cost > lowest:
                continue
            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_cost[(nr, nc, ndr, ndc)] = new_cost
            backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

# Backtrack to find all reachable states
states = deque(end_states)
seen = set(end_states)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen:
            continue
        seen.add(last)
        states.append(last)

# Output the number of unique positions visited
print(len({(r, c) for r, c, _, _ in seen}))
