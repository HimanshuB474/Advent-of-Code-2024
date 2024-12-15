import os

top, bottom = open("input.txt").read().split("\n\n")

grid = [list(line) for line in top.splitlines()]
moves = bottom.replace("\n", "")

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    if "@" in grid[r]:
        c = grid[r].index("@")
        break

for move in moves:
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = []

    cr, cc = r, c
    go = True
    while True:
        cr += dr
        cc += dc
        if grid[cr][cc] == "#":  
            go = False
            break
        elif grid[cr][cc] == "O": 
            targets.append((cr, cc))
        elif grid[cr][cc] == ".":  
            break
    
    if not go: continue

    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets:
        grid[br + dr][bc + dc] = "O"

    r += dr
    c += dc

result = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O")
print(f"\nFinal result: {result}")

os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen to show final grid
print("Final Grid Visualization:")
for row in grid:
    print("".join(row))
