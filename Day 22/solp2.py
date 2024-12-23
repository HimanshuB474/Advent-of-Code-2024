from collections import defaultdict

def step(num):
    # Use bitwise AND for modulo 16777216 (2^24)
    num = (num ^ (num * 64)) & 0xFFFFFF
    num = (num ^ (num // 32)) & 0xFFFFFF
    num = (num ^ (num * 2048)) & 0xFFFFFF
    return num

seq_to_total = defaultdict(int)

for line in open("input.txt"):
    num = int(line)
    buyer = [num % 10]
    
    # Generate the sequence efficiently
    for _ in range(2000):
        num = step(num)
        buyer.append(num % 10)
    
    seen = set()
    buyer_len = len(buyer)
    
    # Precompute differences for sequence generation
    for i in range(buyer_len - 4):
        a, b, c, d, e = buyer[i:i + 5]
        seq = (b - a, c - b, d - c, e - d)
        if seq in seen:
            continue
        seen.add(seq)
        seq_to_total[seq] += e

# Find and print the maximum value in seq_to_total
print(max(seq_to_total.values()))
