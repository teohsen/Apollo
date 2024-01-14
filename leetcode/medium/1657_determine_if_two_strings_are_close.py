from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        test = Solution()
        word1 = "abbzccca"
        word2 = "babzzczc"


        word1 = "uau"
        word2 = "ssx"
        print(test.closeStrings(word1, word2))

        :param word1:
        :param word2:
        :return:
        """

        w1 = Counter(word1)
        w2 = Counter(word2)

        v1 = sorted(list(w1.values()))
        v2 = sorted(list(w2.values()))
        w1 = sorted(list(w1.keys()))
        w2 = sorted(list(w2.keys()))

        if v1 == v2 and w1 == w2:
            return True

        return False


    def closeStrings2(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        if sorted(w1.keys()) == sorted((w2.keys())) and sorted(w1.values()) == sorted(w2.values()):
            return True

        return False