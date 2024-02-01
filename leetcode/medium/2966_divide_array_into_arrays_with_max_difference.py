from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(0, len(nums), 3):
            p0 = nums[i]
            p1 = nums[i+1]
            p2 = nums[i+2]

            if (p1 - p0 > k) or (p2 - p1 > k) or (p2 - p0 > k):
                return []

            result.append([p0, p1, p2])

        return result
