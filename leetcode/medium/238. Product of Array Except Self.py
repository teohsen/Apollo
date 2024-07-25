from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        result_right = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            result_right[i] = result_right[i+1] * nums[i+1]

        r = []
        for i,j in zip(result, result_right):
            r.append(i*j)


        return r