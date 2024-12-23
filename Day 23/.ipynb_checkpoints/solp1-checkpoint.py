from collections import defaultdict

# Build the connections graph
edges = [line.strip().split("-") for line in open("input.txt")]
conns = defaultdict(set)

for x, y in edges:
    conns[x].add(y)
    conns[y].add(x)

# Find unique triangles
sets = set()

for x in conns:
    for y in conns[x]:
        for z in conns[y]:
            if z != x and z in conns[x]:
                # Add the sorted tuple to ensure unique representation
                sets.add(tuple(sorted([x, y, z])))

# Count triangles containing a node starting with 't'
result = sum(1 for s in sets if any(node.startswith("t") for node in s))

print(result)
