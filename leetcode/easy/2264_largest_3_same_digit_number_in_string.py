from copy import deepcopy


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1

        for i in range(3, len(num)+1):
            candidate = num[i-3:i]

            if candidate.count(candidate[-1]) == 3:
                result = max(int(candidate[-1]), result)

        return str(result)*3 if result != -1 else ""


    def largestGoodInteger2(self, num: str) -> str:

        num = list(num)
        start, remaining = num[:3], num[3:]

        result = ""
        unique_value = -1

        if start.count(start[0]) == 3:
            result = deepcopy(start)
            unique_value = int(start[0])

        while remaining:
            _ = remaining.pop(0)
            start.pop(0)
            start.append(_)

            # check if candidate is all unique and assign result
            if start.count(_) == 3 and int(_) > unique_value:
                result = deepcopy(start)
                unique_value = int(_)
        return "".join(result)