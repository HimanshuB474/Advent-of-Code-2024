from collections import defaultdict

# Read input from "input.txt"
with open("input.txt", "r") as file:
    stones = [int(x) for x in file.readline().split()]

steps = 75

# Dictionary to store intermediate results
cache = defaultdict(int)

def count(stone, steps):
    # Base case
    if steps == 0:
        return 1
    # Check cache
    if (stone, steps) in cache:
        return cache[(stone, steps)]
    # Process the current stone
    if stone == 0:
        result = count(1, steps - 1)
    else:
        string = str(stone)
        length = len(string)
        if length % 2 == 0:
            result = count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
        else:
            result = count(stone * 2024, steps - 1)
    # Cache the result
    cache[(stone, steps)] = result
    return result

# Compute the result
print(sum(count(stone, steps) for stone in stones))
