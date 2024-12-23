def step(num):
    # Use bitwise AND instead of modulo for faster computation
    num = (num ^ (num * 64)) & 0xFFFFFF
    num = (num ^ (num // 32)) & 0xFFFFFF
    num = (num ^ (num * 2048)) & 0xFFFFFF
    return num

total = 0

# Read input lines and process each number
for line in open("input.txt"):
    num = int(line)
    # Optimize by running the step function 2000 times in a loop
    for _ in range(2000):
        num = step(num)
    total += num

print(total)
