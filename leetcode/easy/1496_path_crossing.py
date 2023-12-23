class Solution:
    def isPathCrossing(self, path: str) -> bool:

        map = {
            "N": 1,
            "S": -1,
            "E": 1,
            "W": -1
        }

        points = [(0, 0)]
        c_x, c_y = 0, 0
        for dir in path:
            if dir in ("N", "S"):
                c_y += map.get(dir)
            if dir in ("E", "W"):
                c_x += map.get(dir)

            if (c_x, c_y) in points:
                return True

            points.append((c_x, c_y))

        return False
