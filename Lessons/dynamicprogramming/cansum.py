memo = {}

def cansum(target, nums):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in nums:
        remainder = target - i
        if cansum(remainder, nums) is True:
            memo[target] = True
            return memo[target]

    memo[target] = False
    return False


print(cansum(1, [2, 4]))
print(memo)