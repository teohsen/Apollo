from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Alg - 2 Pointer
        T - O(n)
        S - O(1)

        :param colors:
        :param neededTime:
        :return:
        """
        # colors = "abaac"
        # neededTime = [1,2,3,4,1]
        #
        # colors = "aabaa"
        # neededTime = [1, 2, 3, 4, 1]

        result = 0
        l = 0

        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    result += neededTime[l]
                    l = r
                else:
                    result += neededTime[r]
            else:
                l = r

        return result








