# Open the input.txt file
with open("input.txt") as file:
    # Parse rules
    rules = []
    cache = set()

    for line in file:
        if line.isspace():
            break  # Stop when we hit an empty line or white space
        x, y = map(int, line.strip().split("|"))
        rules.append((x, y))
        cache.add((x, y))  # x must come before y

    # Function to check if an update list is ordered
    def is_ordered(update):
        n = len(update)
        for i in range(n):
            for j in range(i + 1, n):
                # Check reverse ordering; return early if violated
                if (update[j], update[i]) in cache:
                    return False
        return True

    # Process updates and calculate the total
    total = 0
    for line in file:
        update = list(map(int, line.strip().split(",")))
        if is_ordered(update):
            total += update[len(update) // 2]

    print(total)
