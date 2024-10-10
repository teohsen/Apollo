# 3. Longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cache = set()
        l = 0
        result = 0
        for r, r_v in enumerate(s):
            while r_v in cache:
                cache.remove(s[l])
                l += 1

            cache.add(r_v)
            result = max(result, r - l + 1)

        return result


x = Solution()
s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = ""
# s = " "
print(x.lengthOfLongestSubstring(s))