# Date: 07-05-2023
# Difficulty: Hard
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/

import bisect
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        result = [10**8] * (obstacles.__len__() + 1)

        for obstacle in obstacles:
            idx = bisect.bisect(result, obstacle)
            lis.append(idx + 1)
            result[idx] = obstacle

            print(f"{obstacle}, {idx}, {result}, {lis}")

        return lis


def test():

    soln = Solution()

    def test_1():
        input = [3,1,5,6,4,2]
        expected_output = [1,1,2,3,2,2]

        result = soln.longestObstacleCourseAtEachPosition(input)

        assert result == expected_output
        print("Test 1 : Ok")


    test_1()


if __name__ == "__main__":
    test()
