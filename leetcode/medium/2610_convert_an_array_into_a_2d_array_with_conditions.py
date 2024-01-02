from typing import List
from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        https://www.youtube.com/watch?v=9pl1QiaGgmI&ab_channel=NeetCodeIO
        :return:
        """
        count = defaultdict(int)
        res = []

        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])

            res[row].append(n)
            count[n] += 1

        return res


    def findMatrix2(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        result = {}

        while nums:
            i = nums.pop(0)
            level = cache.get(i, 0)

            ll = result.get(level, [])
            ll.append(i)
            result[level] = ll

            cache[i] = level + 1

        return list(result.values())


    def findMatrix3(self, nums: List[int]) -> List[List[int]]:
        layer = []
        i = 0
        while nums:
            if i > len(nums) - 1:
                break

            if not layer.__contains__(nums[i]):
                layer.append(nums.pop(i))
            else:
                i += 1

        result = [layer]
        if len(nums) > 0:
            result.extend(self.findMatrix(nums))

        return result