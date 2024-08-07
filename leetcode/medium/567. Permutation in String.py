class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        cache = {}
        for i in s1:
            cache[i] = cache.get(i, 0) + 1

        for r in range(len(s1), len(s2)+1):
            l_cache = {}
            for j in s2[l:r]:
                l_cache[j] = l_cache.get(j, 0) + 1
            if cache == l_cache:
                return True

            l += 1

        return False

    def test(self):

        s1 = "ab"
        s2 = "eidbaooo"

        s1 = "adc"
        s2 = "dcda"

        return self.checkInclusion(s1, s2)


print(Solution().test())
