with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

rows, cols = len(grid), len(grid[0])

# Find the starting position
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            break
    else:
        continue
    break

def loops(grid, start_r, start_c):
    dr, dc = -1, 0
    seen = set()

    r, c = start_r, start_c
    while True:
        seen.add((r, c, dr, dc))
        nr, nc = r + dr, c + dc
        
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            return False
        
        if grid[nr][nc] == "#":
            dr, dc = -dr, dc
        else:
            r, c = nr, nc
        
        if (r, c, dr, dc) in seen:
            return True

count = 0
for cr in range(rows):
    for cc in range(cols):
        if grid[cr][cc] != ".": 
            continue
        grid[cr][cc] = "#"
        if loops(grid, r, c):
            count += 1
        grid[cr][cc] = "."

print(count)