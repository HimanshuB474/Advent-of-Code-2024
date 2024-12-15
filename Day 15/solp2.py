top, bottom = open("input.txt").read().split("\n\n")

# Expansion of characters as defined in the problem
expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}

# Initialize the grid by expanding each character in the top
grid = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]
moves = bottom.replace("\n", "")

rows = len(grid)
cols = len(grid[0])

# Locate the initial position of '@' in the grid
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            start_r, start_c = r, c
            break
    else:
        continue
    break

# Function to handle movement of the grid
for move in moves:
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = [(start_r, start_c)]
    go = True

    # Iterate over the targets for this move
    for cr, cc in targets:
        nr, nc = cr + dr, cc + dc
        if (nr, nc) in targets: continue  # Skip already processed targets
        
        char = grid[nr][nc]

        if char == "#":  # Wall hit condition
            go = False
            break
        if char == "[":  # Targeted area found
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if char == "]":  # Targeted area found
            targets.append((nr, nc))
            targets.append((nr, nc - 1))

    # If move is blocked, continue to next move
    if not go: continue
    
    # Make a copy of the grid for updating purposes
    copy = [row[:] for row in grid]
    
    # Move '@' and clear its previous position
    grid[start_r][start_c] = "."
    grid[start_r + dr][start_c + dc] = "@"

    # Update targets' positions
    for br, bc in targets[1:]:
        grid[br][bc] = "."
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = copy[br][bc]

    start_r += dr
    start_c += dc

# Final calculation and output the result
result = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "[")
print(result)
