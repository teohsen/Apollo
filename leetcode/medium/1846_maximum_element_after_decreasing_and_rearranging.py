from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort(reverse=False)

        prev_n = 0
        for n in arr:
            prev_n = min(prev_n + 1, n)   # ensures 0 [ 3, 4, 5], the left most/ starting is 1
        return prev_n

        # Alternative
        # result = 1
        # for i in range(1,len(arr)):
        #     print(i, arr[i], result)
        #
        #     if (arr[i] > result):
        #         result += 1
        # return result