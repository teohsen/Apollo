from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        perimeter = -1

        for num in nums:
            print(num, sum_val, num<sum_val)
            if num < sum_val:
                perimeter = num + sum_val
            sum_val += num

        return perimeter


test = Solution()
nums = [1,12,1,2,5,50,3]
# nums = [5, 5, 5]
# nums = [5, 5, 50]
# nums = [5, 50, 5]
#nums = [1,1,2]
print(test.largestPerimeter(nums))