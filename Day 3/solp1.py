import re

# Open and read from input.txt
with open("input.txt", "r") as file:
    memory = file.read()

total = 0

# Find all matches for the pattern mul(x,y)
for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory):
    # Extract the numbers x and y
    x, y = map(int, match[4:-1].split(","))
    # Add their product to the total
    total += x * y

# Print the total
print(total)
