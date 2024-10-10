class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        cache = {}
        result = 0
        l = 0
        most_freq = 0
        for r in range(len(s)):
            cache[s[r]] = cache.get(s[r], 0) + 1
            most_freq = max(most_freq, cache[s[r]])

            while (r - l + 1) - most_freq > k:
                cache[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)  # r-l+1 --> size of window


        return result