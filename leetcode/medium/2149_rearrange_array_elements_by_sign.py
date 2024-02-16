from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos = [_ for _ in nums if _ > 0]
        # neg = [_ for _ in nums if _ < 0]

        pos = []
        neg = []

        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        c = 0
        for i in range(0, len(pos)):
            nums[c] = pos[i]
            nums[c+1] = neg[i]
            c += 2

        return nums


