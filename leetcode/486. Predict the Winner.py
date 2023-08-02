from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = nums.__len__()
        stage = [0] * n

        for i in range(n-1, -1, -1):
            print(i)
            stage[i] = nums[i]
            for j in range(i+1, n):
                stage[j] = max(nums[i] - stage[j],
                               nums[j] - stage[j-1])

    def PredictTheWinner_DP_TP(self, nums: List[int]):

        n = nums.__len__()
        memo = {}

        def max_diff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]

            left_score = nums[left] - max_diff(left+1, right)
            right_score = nums[right] - max_diff(left, right-1)
            memo[(left, right)] = max(left_score, right_score)
            return memo[(left, right)]

        return max_diff(0, n-1) >= 0

    def PredictTheWinner_DP_BU(self, nums):
        # TODO:
        pass
