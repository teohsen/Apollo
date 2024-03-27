from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = [1, 2, 2, 1]
        # nums2 = [2, 2]
        return list(set(nums1) & set(nums2))