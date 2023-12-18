from typing import List
import heapq
from math import prod

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums = [5, 6, 2, 7, 4]
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


    def maxProductDifference2(self, nums: List[int]) -> int:
        # nums = [5, 6, 2, 7, 4]
        return prod(heapq.nlargest(2, nums)) - prod(heapq.nsmallest(2, nums))