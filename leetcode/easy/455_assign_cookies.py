from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1

        return i

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        j = 0

        for i in g:
            while j < len(s):
                if s[j] >= i:
                    result += 1
                    j += 1
                    break
                else:
                    j += 1

        return result


    def findContentChildren3(self, g: List[int], s: List[int]) -> int:

        result = 0
        if len(s) == 0:
            return result

        s.sort()

        for i in range(len(g)):
            greed = g[i]

            for index, sat in enumerate(s):
                if sat >= greed:
                    result += 1
                    s.pop(index)
                    break

        return result




