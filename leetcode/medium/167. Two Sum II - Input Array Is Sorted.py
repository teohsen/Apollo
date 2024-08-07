from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l , r = 0, len(numbers) -1
        while l < r:
            v = numbers[l] + numbers[r]
            if v == target:
                break
            if v > target:
                r -= 1
            elif v < target:
                l += 1


        return [l+1, r+1]
