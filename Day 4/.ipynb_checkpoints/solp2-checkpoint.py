grid = open("input.txt").read().splitlines()

count = 0
rows = len(grid)
cols = len(grid[0])

# Loop over the positions, skipping the borders to avoid out-of-bound errors
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if grid[r][c] == "A":
            # Efficiently check the corners surrounding the 'A'
            corners = [grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r + 1][c - 1]]
            # Convert the corner list to a string and check if it matches any of the patterns
            if "".join(corners) in {"MMSS", "MSSM", "SSMM", "SMMS"}:
                count += 1

print(count)
