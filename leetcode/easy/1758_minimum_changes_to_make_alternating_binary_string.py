from itertools import cycle

class Solution:
    def minOperations(self, s: str) -> int:
        # s = "1111"
        # s = "0100"
        # s = "10010100"

        nxt_0 = cycle(["0", "1"])
        nxt_1 = cycle(["1", "0"])

        result_0 = 0
        result_1 = 0

        for i in s:
            if i != nxt_0.__next__():
                result_0 += 1
            if i != nxt_1.__next__():
                result_1 += 1

        return min(result_0, result_1)


    def minOperations2(self, s: str) -> int:
        nxt_0 = cycle("01")
        result_0 = 0

        for i in s:
            if i == nxt_0.__next__():
                result_0 += 1

        # a, b = "0", "1"
        # result_0 = 0
        #
        # for i in s:
        #     if i == a:
        #         result_0 += 1
        #
        #     b, a = a, b

        return min(result_0, len(s) - result_0)