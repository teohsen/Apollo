from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1

        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        ans += 1

        return ans

    # Cool
    def numSpecial2(self, mat: List[List[int]]) -> int:
        v = [i for i, r in enumerate(mat) if sum(r) == 1]
        h = [i for i, c in enumerate(zip(*mat)) if sum(c) == 1]
        return sum(mat[r][c] for r in v for c in h)