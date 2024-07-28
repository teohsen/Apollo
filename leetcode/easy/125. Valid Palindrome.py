import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


    def isPalindrome2(self, s: str) -> bool:
        s = "A man, a plan, a canal: Panama"

        s = "".join(re.findall("[a-z0-9]", s.lower()))
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False

        return True

