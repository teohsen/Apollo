from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = Counter(nums)
        return True if n.most_common(1)[0][1] == 1 else False


    def containDuplicateAlt(self, nums):
        rr = {}
        for i in nums:
            if rr.__contains__(i):
                return True
            else:
                rr[i] = None

        return False