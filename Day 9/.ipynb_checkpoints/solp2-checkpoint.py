files = {}
blanks = []

fid = 0
pos = 0

# Read input from a file
with open('input.txt', 'r') as file:
    data = file.read().strip()

# Process the input to track files and blanks
for i, char in enumerate(data):
    x = int(char)
    if i % 2 == 0:
        if x == 0:
            raise ValueError("unexpected x=0 for file")
        files[fid] = (pos, x)  # Track file positions and sizes
        fid += 1
    else:
        if x != 0:
            blanks.append((pos, x))  # Track blank positions and lengths
    pos += x

# Fill blanks with files from the end
while fid > 0:
    fid -= 1
    pos, size = files[fid]
    for i, (start, length) in enumerate(blanks):
        if start >= pos:
            blanks = blanks[:i]
            break
        if size <= length:
            files[fid] = (start, size)
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break

# Calculate the total score
total = 0
for fid, (pos, size) in files.items():
    for x in range(pos, pos + size):
        total += fid * x

# Output the total score
print(total)