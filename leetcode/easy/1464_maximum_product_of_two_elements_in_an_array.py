from typing import List
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums = [3, 4, 5, 2]
        nums.sort(reverse=True)
        return (nums[0]-1)*(nums[1]-1)

    def maxProduct2(self, nums: List[int]) -> int:
        # nums = [3, 4, 5, 2]
        # heapq.heapify(nums)
        i, j = heapq.nlargest(2, nums)
        return (i-1) * (j-1)

    def maxProduct3(self, nums: List[int]) -> int:
        # nums = [3, 4, 5, 2]
        i = max(nums)
        nums.remove(i)
        j = max(nums)

        return (i-1) * (j-1)