from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:


        # points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
        # points = [[8,7],[9,9],[7,4],[9,7]]

        points = list(set([_[0] for _ in points]))
        points.sort()

        #points = sorted(points, key=lambda x: x[0])
        result = 0

        for i in range(1, len(points)):
            result = max(points[i] - points[i-1], result)

        return result