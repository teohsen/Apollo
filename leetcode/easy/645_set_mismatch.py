from typing import List
from collections import Counter

class Solution:
    # nums = [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
    # nums = [1, 1]
    def findErrorNums(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)

        for i in nums:
            result[i-1] += 1

        x = [0, 0]
        for index, i in enumerate(result, start=1):
            if i == 0:
                x[1] = index
            if i == 2:
                x[0] = index

        return x
    def findErrorNums2(self, nums: List[int]) -> List[int]:
        dupe = Counter(nums).most_common(1)[0][0]
        missing = set([i for i in range(1, len(nums)+1)]).difference(nums).pop()

        return [dupe, missing]
