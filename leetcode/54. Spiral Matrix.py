# Date : 09-05-2023
# Difficulty : Medium
# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        # matrix = [[2, 3]]
        # matrix = [[2], [3]]
        # matrix = [[1,2,3,4],
        #           [5,6,7,8],
        #           [9,10,11,12],
        #           [13,14,15,16]]

        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]  # Rotate anti-clockwise 90 degree
            # Reference: https://medium.com/@SantalTech/a-clever-one-liner-to-rotate-2d-arrays-in-python-f67608ec77f9
            # list(zip(*matrix[::-1])) <- Rotate clockwise 90 degree

        return res
