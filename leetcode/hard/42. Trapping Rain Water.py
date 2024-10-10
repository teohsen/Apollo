from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

        l = 0
        r = len(height) - 1
        lm = height[l]
        rm = height[r]

        total_volume = 0

        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                total_volume += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                total_volume += rm - height[r]

        return total_volume
