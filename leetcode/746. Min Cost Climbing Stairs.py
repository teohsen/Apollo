from typing import List

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Recall Fib seq where nth step depends on n-1 and n-2 step

        :param cost:
        :return:
        """
        step_0, step_1 = cost[0], cost[1]

        for cst in cost[2:]:
            step_0, step_1 = step_1, min(step_0, step_1)+cst

        return min(step_0, step_1)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = cost.__len__()
        dp = [-1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0  # constraint 2 <= cost.length <= 1000, directly set 0

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
            print(i, dp)

        return dp[n]



sol = Solution()
test_cases = [
    ([10, 15, 20], 15),
    ([15, 10, 20], 10),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
]

for input_test, answer in test_cases:
    result = sol.minCostClimbingStairs2(input_test)
    print(f"{answer = }, {result = }, { answer.__eq__(result) }")
