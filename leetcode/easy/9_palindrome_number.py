class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x: int) -> bool:
        x = str(x)
        n = len(x)

        for i in range(0, len(x)//2):
            l = x[i]
            r = x[n-1-i]
            if l != r:
                return False

        return True

