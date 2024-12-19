lines = open("input.txt").read().splitlines()

patterns = set(lines[0].split(", "))
maxlen = max(map(len, patterns))

def num_possibilities(design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: there's 1 way to construct an empty string.

    for i in range(1, n + 1):
        for j in range(max(0, i - maxlen), i):
            if design[j:i] in patterns:
                dp[i] += dp[j]

    return dp[n]

result = sum(num_possibilities(design) for design in lines[2:])
print(result)
