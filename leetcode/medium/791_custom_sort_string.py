class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # order = "bcafg"
        # s = "abcd"
        result = ""
        for i in order:
            if i in s:
                result += i * s.count(i)
                s = s.replace(i,"")

        return result + s
