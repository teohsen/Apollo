class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        q = []

        for p in s:
            if p not in mapper:
                q.append(p)
                continue

            if not q or q[-1] != mapper.get(p):
                return False

            q.pop()

        return not q


