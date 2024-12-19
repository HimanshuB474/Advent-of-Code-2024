lines = open("input.txt").read().splitlines()

patterns = set(lines[0].split(", "))
maxlen = max(map(len, patterns))

def can_obtain(design):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: an empty string can always be obtained.

    for i in range(1, n + 1):
        for j in range(max(0, i - maxlen), i):
            if dp[j] and design[j:i] in patterns:
                dp[i] = True
                break

    return dp[n]

result = sum(1 for design in lines[2:] if can_obtain(design))
print(result)
