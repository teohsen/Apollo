from copy import deepcopy

def howsum(tt, nn):
    memo = {}

    def core(target, nums):
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        if target < 0:
            return None

        for i in nums:
            remainder = target - i
            result = core(remainder, nums)
            if result is not None:
                n = deepcopy(result)
                n.append(i)
                memo[target] = n
                return memo[target]

        memo[target] = None
        return None

    return core(tt, nn)


print(howsum(7, [5,3,4,7]))  # --> [3, 4], [7]
print(howsum(8, [2,3, 5])) # --> [3, 5], [2,2,2,2]
print(howsum(7, [2,4]))  # --> None
print(howsum(0, [1,2,3]))  # --> []
print(howsum(1001, [2]))  # --> None
