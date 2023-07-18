from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * nums.__len__()
        _ = 1
        for i in range(nums.__len__()):
            res[i] = _
            _ = _ * nums[i]
        _ = 1
        for i in range(nums.__len__()-1, -1, -1):
            res[i] *= _
            _ *= nums[i]
        return res