from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # bank = ["011001", "000000", "010100", "001000"]
        # bank = ["000","111","000"]

        result = 0
        l_sum = 0
        for r in range(len(bank)):
            r_sum = bank[r].count("1")
            if r_sum == 0:
                continue

            result += (l_sum * r_sum)
            l_sum = r_sum

        return result

    def numberOfBeams2(self, bank: List[str]) -> int:
        """
        https://www.youtube.com/watch?v=KLeKv59LAFY&ab_channel=NeetCodeIO

        Time: O(N * M)
        Mem: O(1)

        :param bank:
        :return:
        """
        prev = bank[0].count("1")
        res = 0
        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                res += (prev * curr)
                prev = curr

        return res