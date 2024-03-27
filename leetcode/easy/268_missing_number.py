from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(0, len(nums)+1)]) - sum(nums)


    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)