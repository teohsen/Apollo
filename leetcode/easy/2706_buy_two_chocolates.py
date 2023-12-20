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