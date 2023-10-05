from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = nums.__len__()/3
        result = []

        for k, v in Counter(nums).items():
            if v > n:
                result.append(k)

        return result

    def majorityElementTwo(self, nums):
        threshold = nums.__len__()//3
        return [k for k, v in Counter(nums).items() if v > threshold]

