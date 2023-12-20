from typing import List
import heapq

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a, b = heapq.nsmallest(2, prices)
        remaining = money - (a + b)


        return money if remaining < 0 else remaining


    def buyChoco2(self, prices: List[int], money: int) -> int:
        prices.sort()
        _ = money - (prices[0] + prices[1])
        if _ < 0:
            return money

        return _

    def buyChoco3(self, prices: List[int], money: int) -> int:

        min_1 = float("inf")
        min_2 = float("inf")


        for p in prices:
            if p < min_1:
                min_2 = min_1
                min_1 = p
            elif p < min_2:
                min_2 = p

            # do nothing if neither
        return remaining if (remaining:= money - min_1 - min_2) >= 0 else money
