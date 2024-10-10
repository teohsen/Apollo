# 121 best_time_to_buy_and_sell_stock_121

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        lowest = prices[0]
        for p in prices:
          if p <= lowest:
            lowest = p
          result = max(result, p - lowest)

        return result


x = Solution()
prices = [7,1,5,3,6,4]
#prices = [7,6,5,4,3,2,1]
print(x.maxProfit(prices))