from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index, i in enumerate(nums):
            find = target - i
            if nums.__contains__(find):
                j = nums.index(find)
                if j == index:
                    continue
                break

        return [index, j]