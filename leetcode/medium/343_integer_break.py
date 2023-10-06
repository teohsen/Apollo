"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.
"""
from math import pow


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        num_of_three = (n // 3)
        rem_of_three = n % 3
        if rem_of_three == 1:
            result = int(pow(3, num_of_three-1) * 4)
        elif rem_of_three == 2:
            result = int(pow(3, num_of_three) * 2)
        else:
            result = int(pow(3, num_of_three))

        return result
