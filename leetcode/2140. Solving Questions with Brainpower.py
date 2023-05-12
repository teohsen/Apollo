from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]

        qlen = len(questions)
        score = [0] * qlen

        def branch(i):
            if i >= qlen:
                # input value greater than length of questions
                return 0

            if score[i]:
                # if cached, score[i] != 0 which will not return False, return the saved value
                return score[i]

            # Not out of bound and not memorized, need to calculate

            p, bp = questions[i]

            score[i] = max(branch(i+1), branch(i+bp+1)+p)

            print(f"{i = }, {p = }, {bp = }, {score[i] = }, {branch(i+1) = }, {branch(i+bp+1)+p =}")

            return score[i]

        return branch(0)

    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
        4 5 5
        [0, 0, 0, 0, 5, 0] 5
        3 4 4
        [0, 0, 0, 5, 5, 0] 5
        2 3 3
        [0, 0, 5, 5, 5, 0] 5
        1 2 2
        [0, 7, 5, 5, 5, 0] 4
        0 1 1
        [7, 7, 5, 5, 5, 0] 2
        """
        n = questions.__len__()

        scores = [0] * (n+1)

        for i in range(n-1, -1, -1):
            p, bp = questions[i]
            nxt_step = min(i+bp+1, n)
            step_point = p + scores[nxt_step]
            scores[i] = max(step_point, scores[i+1])

        return scores[0]
