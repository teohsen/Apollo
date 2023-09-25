from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if s.__len__().__eq__(0):
            return t

        return list((Counter(t) - Counter(s)).keys())[0]

    def solution_2(self, s, t):
        """
        unicode method

        :param s:
        :param t:
        :return:
        """
        sum_s = 0
        sum_t = 0

        for _ in s:
            sum_s += ord(_)

        for _ in t:
            sum_t += ord(_)

        return chr(sum_t - sum_s)

    def test(self):
        s = "abcd"
        t = "abcde"

        result = self.findTheDifference(s, t)
        print(result)

        result = self.solution_2(s, t)
        print(result)


Solution().test()
