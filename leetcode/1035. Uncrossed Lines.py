# Date : 11-05-2023
# Difficulty : Medium
# https://leetcode.com/problems/uncrossed-lines/

"""
LCS
Dynamic Programming
Tabulation
"""


class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        n1 = nums1.__len__()
        n2 = nums2.__len__()

        """
        calculates the entire table
        """
        dp = [[0] * (n2+1) for _ in range(n1 + 1)]

        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[n1][n2]


    def maxUncrossedLinesMemOptimized(self, nums1, nums2):
        n1 = nums1.__len__()
        n2 = nums2.__len__()

        """
        Only require 2 rows of array at any time.
        """

        prior_dp = [0] * (n2+1)

        for i in range(n1):
            current_dp = [0] * (n2+1)
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    current_dp[j+1] = 1 + prior_dp[j]
                else:
                    current_dp[j+1] = max(current_dp[j], prior_dp[j+1])

            prior_dp = current_dp
        return prior_dp[n2]
