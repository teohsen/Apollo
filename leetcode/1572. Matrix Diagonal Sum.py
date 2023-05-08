# Date: 08-05-2023
# Difficulty: Easy
# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List


class Solution:
    # Iter 1: Loop through full length of mat and subtract middle
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        mat_length = len(mat)

        for i in range(mat_length):
            ans += mat[i][i] + mat[i][mat_length-i-1]

        if mat_length%2 == 1:
            ans -= mat[mat_length//2][mat_length//2]

        return ans

    # Iter 2: Loop half length of mat and add middle
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        mat_length = mat.__len__()

        for i in range(mat_length//2):
            ans += mat[i][i] + mat[i][-1-i] + mat[-1-i][i] + mat[-1-i][-1-i]

        if mat_length % 2 == 1:
            ans += mat[mat_length//2][mat_length//2]

        return ans