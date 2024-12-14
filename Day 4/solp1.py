grid = open("input.txt").read().splitlines()

count = 0
rows = len(grid)
cols = len(grid[0])

# Loop over all positions in the grid
for r in range(rows):
    for c in range(cols):
        # Check only if the current position is 'X'
        if grid[r][c] == "X":
            # Check all 8 possible directions
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    
                    # Ensure the three subsequent steps are within bounds
                    if 0 <= r + 3 * dr < rows and 0 <= c + 3 * dc < cols:
                        # Check if the pattern matches (M, A, S) in the specific direction
                        if (grid[r + dr][c + dc] == "M" and
                            grid[r + 2 * dr][c + 2 * dc] == "A" and
                            grid[r + 3 * dr][c + 3 * dc] == "S"):
                            count += 1

print(count)
