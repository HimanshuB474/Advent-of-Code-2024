def safe(levels):
    increasing = decreasing = True
    for x, y in zip(levels, levels[1:]):
        diff = x - y
        if not (1 <= diff <= 3):  # Not strictly increasing
            increasing = False
        if not (-3 <= diff <= -1):  # Not strictly decreasing
            decreasing = False
        if not (increasing or decreasing):  # If neither holds, break early
            return False
    return True

count = 0

# Open and read from input.txt
with open("input.txt", "r") as file:
    for report in file:
        levels = list(map(int, report.split()))
        if safe(levels):
            count += 1

print(count)
