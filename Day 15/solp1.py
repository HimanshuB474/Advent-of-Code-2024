top, bottom = open("input.txt").read().split("\n\n")

grid = [list(line) for line in top.splitlines()]
moves = bottom.replace("\n", "")

rows = len(grid)
cols = len(grid[0])

# Find the start position of "@"
for r in range(rows):
    if "@" in grid[r]:
        c = grid[r].index("@")
        break

# Process each move
for move in moves:
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = []
    
    # Initialize current position
    cr, cc = r, c
    go = True
    while True:
        cr += dr
        cc += dc
        if grid[cr][cc] == "#":  # Wall hits
            go = False
            break
        elif grid[cr][cc] == "O":  # Target found
            targets.append((cr, cc))
        elif grid[cr][cc] == ".":  # Empty space
            break
    
    if not go: continue
    
    # Update grid: move '@', place "O" on targets
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets:
        grid[br + dr][bc + dc] = "O"
    
    # Update the current position of '@'
    r += dr
    c += dc

# Compute the result after all moves
result = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O")
print(result)

