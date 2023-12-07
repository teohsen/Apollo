class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        check last digit right to left - Odd Digit

        :param num: Input value
        :return: largest Odd Digit string
        """
        for i in range(len(num)-1, -1 , -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]

        return ""
