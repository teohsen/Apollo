from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        valid = "123456789"
        for i in range(len(str(low)), len(str(high))+1):
            for j in range(10-i):
                _ = int(valid[j:j+i])
                if low <= _ <= high and len(str(_)) == i:
                    result.append(_)

        return result


    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        # brute force,
        # checks every integer
        def check_value(input):
            x = list(str(input))
            for i in range(1, len(x)):
                if int(x[i]) - int(x[i-1]) != 1:
                    return False
            return True


        result = []
        for i in range(low, high+1):
            if check_value(i):
                result.append(i)

        return result
