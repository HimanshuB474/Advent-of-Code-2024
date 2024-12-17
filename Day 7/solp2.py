total = 0

def can_obtain(target, array, memo):
    # Use a memoization key based on current target and remaining array
    key = (target, len(array))
    if key in memo:
        return memo[key]

    if len(array) == 1:
        memo[key] = (target == array[0])
        return memo[key]

    if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1], memo):
        memo[key] = True
        return True

    if target > array[-1] and can_obtain(target - array[-1], array[:-1], memo):
        memo[key] = True
        return True

    s_target = str(target)
    s_last = str(array[-1])
    if s_target.endswith(s_last) and len(s_target) > len(s_last) and can_obtain(int(s_target[:-len(s_last)]), array[:-1], memo):
        memo[key] = True
        return True

    memo[key] = False
    return False

for line in open("input.txt"):
    l, r = line.split(": ")
    target = int(l)
    array = [int(x) for x in r.split()]
    
    # Pass a memoization dictionary
    if can_obtain(target, array, {}):
        total += target

print(total)
