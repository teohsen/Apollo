class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for s1, t1 in zip(s, t):
            if smap.__contains__(s1) is False and tmap.__contains__(t1) is False:
                smap[s1] = t1
                tmap[t1] = s1
            elif smap.get(s1) != t1 or tmap.get(t1) != s1:
                return False

        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.index, s)) == list(map(t.index, t))
