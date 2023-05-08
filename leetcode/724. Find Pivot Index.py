# LeetCode 75
# Difficulty: Easy
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        ans = -1
        for idx, val in enumerate(nums):
            print(idx, val, left_sum, right_sum)
            right_sum -= val
            if left_sum == right_sum:
                ans = idx
                break
            left_sum += val

        return ans
