import heapq
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        output = 0
        used_frequencies = set()

        heap = list(cnt.values())
        heapq.heapify(heap)

        while heap:
            freq = heapq.heappop(heap)
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                output += 1
            used_frequencies.add(freq)

        return output

    def BRUTEFORCE_minDeletions(self, s: str) -> int:
        output = 0
        count_list = sorted(list(Counter(s).values()), reverse=True)
        length = count_list.__len__()
        if length.__eq__(1):
            return output

        for j in range(1, count_list.__len__() + 1):
            if j.__eq__(length):
                left = count_list[-2]
                right = count_list[-1]

                if right >= left:
                    output += right - left + 1
            else:
                left = count_list[j-1]  # 25
                right = count_list[j]   # 26

                if right.__ge__(left):
                    count_list[j] = min(left, right) - 1
                    output += right - left + 1

                    if count_list[j] == 0:
                        output += sum(count_list[j:])
                        break
        return output
