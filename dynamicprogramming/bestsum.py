from copy import deepcopy
def bestsum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None

    for i in nums:
        remainder = target -i
        result = bestsum(remainder, nums, memo)
        if result is not None:
            n = deepcopy(result)
            n.append(i)
            if shortest is None or (result.__len__() < shortest.__len__()):
                shortest = n

    memo[target] = shortest
    return shortest

# m = target sum
# n = length of num

# Bruteforce
# time: O(n^m * m)
# space: O(m x m)

# memoized
# time: O(m * n * m)
# space: O(m^2)


print(bestsum(7, [5,3,4,7]))
print(bestsum(8, [1,4,5]))
print(bestsum(100, [1,2,5,25]))

