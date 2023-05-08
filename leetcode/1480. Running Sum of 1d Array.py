# LeetCode 75
# Difficulty: Easy
# https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(1, nums.__len__()):
            nums[idx] += nums[idx-1]

        return nums
