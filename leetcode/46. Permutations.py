from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums.__len__() == 1:
            return [nums[:]]
        if nums.__len__() == 0 or None:
            return []

        answer = []
        for i in range(nums.__len__()):
            n = nums.pop(0)
            result = self.permute(nums)

            for p in result:
                p.append(n)

            answer.extend(result)
            nums.append(n)

        return answer

    def permute_soln_alt(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
