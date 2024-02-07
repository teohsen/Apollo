from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # s = "Aabb"
        # s = "tree"
        return "".join([e * c for e, c in Counter(s).most_common()])