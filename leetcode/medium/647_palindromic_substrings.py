class Solution:
    def countSubstrings(self, s: str) -> int:
        cache = set()
        result = 0

        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                t = s[i:j]
                if t in cache or len(t) == 1:
                    result +=1
                    continue

                if t == t[::-1]:
                    result += 1
                    cache.add(t)

        return result