# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        # Peak
        left, right = 1, length-2   # Not initalize at 0, length-1 as the edge elements will never be the peak

        while left <= right:
            mid = (left + right) // 2
            left_val, mid_val, right_val = mountain_arr.get(mid - 1), mountain_arr.get(mid), mountain_arr.get(mid+1)
            if left_val < mid_val < right_val:
                left = mid + 1
            elif left_val > mid_val > right_val:
                right = mid - 1
            else:
                break

        peak = mid

        # left part
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid

        # right part
        left, right = peak, length-1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val < target:
                left = mid - 1
            elif val > target:
                right = mid + 1
            else:
                return mid

        return -1
