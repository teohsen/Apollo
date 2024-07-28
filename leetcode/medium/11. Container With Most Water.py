from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        area = 0
        while l < r:
            area = max(area, min(height[l], height[r]) * (r-1))

            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1

        return area