from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0

        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums[i_index:]):
                if i == j and i_index < j_index+i_index:
                    pairs += 1

        return pairs

    def numIdenticalPairsAlternate(self, nums: List[int]) -> int:
        pairs = 0

        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if nums[i] == nums[j] and i < j:
                    pairs += 1

        return pairs

    def test(self):
        nums = [1, 2, 3, 1, 1, 3]
        output = 4

        print(self.numIdenticalPairsAlternate(nums) == output)
