from typing import List
from math import floor

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        # def get_cell(x, y):
        #     if not (x < 0 or x > m-1 or y < 0 or y > n-1):
        #         return img[x][y]

        # img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]

        m = len(img)
        n = len(img[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                cell = []

                # cell = [_ for x in range(i-1, i+2) for y in range(j-1, j+2) if (_ := get_cell(x, y)) ]
                # or
                # cell = [get_cell(x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)]
                # cell = [_ for _ in cell if _ is not None]

                for i_x in range(i-1, i+2):
                    for j_y in range(j-1, j+2):
                        if i_x < 0 or i_x > m-1 or j_y < 0 or j_y > n-1:
                            continue
                        cell.append(img[i_x][j_y])

                result[i][j] = floor(sum(cell)/len(cell))

        return result


    def imageSmoother2(self, img: List[List[int]]) -> List[List[int]]:
        """
        Using img to store values using bit manipulation

        :param img:
        :return:
        """
        rows = len(img)
        cols = len(img[0])

        for r in range(rows):
            for c in range(cols):

                total = 0
                cnt = 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0 or i == rows or j < 0 or j == cols:
                            continue

                        total += img[i][j] % 256
                        cnt += 1

                img[r][c] = img[r][c] ^ (total // cnt) << 8   # | OR   , ^ XOR, << 8 shift left by 8 bits

        for r in range(rows):
            for c in range(cols):
                img[r][c] = img[r][c] >> 8

        return img
