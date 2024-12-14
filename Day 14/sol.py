import re

WIDTH = 101
HEIGHT = 103

robots = []

# Read input from file
for line in open("input.txt"):  # Change to "text.txt" if your input file name differs
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

min_sf = float("inf")
best_iteration = None

# Iterate through all possible seconds
for second in range(WIDTH * HEIGHT):
    result = []
    
    # Update positions based on velocity and current time step
    for px, py, vx, vy in robots:
        result.append(((px + vx * second) % WIDTH, (py + vy * second) % HEIGHT))
    
    tl = bl = tr = br = 0
    VM = (HEIGHT - 1) // 2  # Vertical midpoint
    HM = (WIDTH - 1) // 2   # Horizontal midpoint

    # Count the number of robots in each quadrant
    for px, py in result:
        if px == HM or py == VM:  # Skip robots on central axes
            continue
        if px < HM:
            if py < VM:
                tl += 1
            else:
                bl += 1
        else:
            if py < VM:
                tr += 1
            else:
                br += 1

    # Calculate scoring function
    sf = tl * bl * tr * br
    
    # Check if this is the minimal score
    if sf < min_sf:
        min_sf = sf
        best_iteration = second

# Output the minimal scoring function value and the corresponding iteration
print(min_sf, best_iteration)

    
            