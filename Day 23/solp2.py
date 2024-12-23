edges = [line.strip().split("-") for line in open("input.txt")]
from collections import defaultdict

# Initialize the connections graph
conns = defaultdict(set)
for x, y in edges:
    conns[x].add(y)
    conns[y].add(x)

# Store unique sets of connected nodes
sets = set()

def search(node, req):
    # Use a frozen set for immutability and efficient storage
    key = frozenset(req)
    if key in sets:
        return
    sets.add(key)
    for neighbor in conns[node]:
        if neighbor in req:
            continue
        # Ensure the neighbor is connected to all nodes in req
        if not all(neighbor in conns[query] for query in req):
            continue
        search(neighbor, req | {neighbor})  # Use set union for clarity

# Start the search from each node
for x in conns:
    search(x, {x})

# Find the largest set and sort it for the output
largest_set = max(sets, key=len)
print(",".join(sorted(largest_set)))
