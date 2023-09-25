from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if s.__len__().__eq__(0):
            return t

        return list((Counter(t) - Counter(s)).keys())[0]

    def test(self):
        s = "abcd"
        t = "abcde"

        result = self.findTheDifference(s, t)
        print(result)


Solution().test()
