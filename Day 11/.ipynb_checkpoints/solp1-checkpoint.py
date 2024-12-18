from collections import deque

# Read input from the file
with open("input.txt", "r") as file:
    stones = deque(map(int, file.readline().split()))

# Process the stones
for _ in range(25):
    output = deque()
    while stones:
        stone = stones.popleft()
        if stone == 0:
            output.append(1)
        else:
            string = str(stone)
            length = len(string)
            if length % 2 == 0:
                mid = length // 2
                output.append(int(string[:mid]))
                output.append(int(string[mid:]))
            else:
                output.append(stone * 2024)
    stones = output

# Output the result
print(len(stones))
