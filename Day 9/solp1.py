disk = []
fid = 0

# Read input from a file
with open('input.txt', 'r') as file:
    data = file.read().strip()

# Process the input to generate the initial disk configuration
for i, char in enumerate(data):
    x = int(char)
    if i % 2 == 0:
        disk += [fid] * x  # Add fid x times to the disk
        fid += 1
    else:
        disk += [-1] * x  # Add blanks (-1) x times to the disk

# Identify blank positions in the disk
blanks = [i for i, x in enumerate(disk) if x == -1]

# Fill in the blanks with valid values from the end of the disk
for i in blanks:
    while disk and disk[-1] == -1:  # Remove trailing blanks
        disk.pop()
    if len(disk) <= i:  # If the disk is shorter than the index, stop
        break
    disk[i] = disk.pop()  # Assign a value to the blank

# Calculate and output the final score
print(sum(i * x for i, x in enumerate(disk)))
