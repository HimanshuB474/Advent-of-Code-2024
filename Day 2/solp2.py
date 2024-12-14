def safe(levels):
    increasing = decreasing = True
    for x, y in zip(levels, levels[1:]):
        diff = x - y
        if not (1 <= diff <= 3):
            increasing = False
        if not (-3 <= diff <= -1):
            decreasing = False
        if not (increasing or decreasing):
            return False
    return True

def is_almost_safe(levels):
    if safe(levels):
        return True
    for index in range(len(levels)):
        # Check if removing levels[index] makes the sequence safe
        sublist = levels[:index] + levels[index + 1:]
        if safe(sublist):
            return True
    return False

count = 0

# Open and read from input.txt
with open("input.txt", "r") as file:
    for report in file:
        levels = list(map(int, report.split()))
        if is_almost_safe(levels):
            count += 1

print(count)
