from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        cache = {}
        results = []
        for index, size in enumerate(groupSizes):
            if size in cache:
                cache[size].append(index)
            else:
                cache[size] = [index]

            if cache[size].__len__().__eq__(size):
                results.append(cache[size])
                cache[size] = []

        return results


groupSizes = [3,3,3,3,3,1,3]
test = Solution()
print(test.groupThePeople(groupSizes))