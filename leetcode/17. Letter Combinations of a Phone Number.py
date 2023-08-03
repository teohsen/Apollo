from typing import List

class Solution:
    def letterCombinations_OWN(self, digits: str) -> List[str]:
        """
        ** First time without reference

        :param digits:
        :return:
        """
        mapping_digits = dict(zip([str(_) for _ in range(2, 10)], "abc,def,ghi,jkl,mno,pqrs,tuv,wxyz".split(",")))
        max_length = digits.__len__()

        def dp(digits):
            if digits == "":
                return []
            if digits.__len__() == 1:
                return list(mapping_digits.get(digits))

            ldigits = list(digits)

            result = []
            while ldigits:
                curr_i = ldigits.pop(0)
                curr = list(mapping_digits.get(curr_i))
                child = dp("".join(ldigits))

                for r in curr:
                    for j in child:
                        _ = f"{r}{j}"
                        result.append(f"{r}{j}")

            return result

        sol = dp(digits)
        sol = [_ for _ in sol if _.__len__() == max_length]
        return sol

    def AlternateSolution1(self, digits):
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack_func(idx, current_combination):
            if idx == len(digits):
                result.append(current_combination[:])
                return

            for letter in digit_to_letters[digits[idx]]:
                print(letter, idx + 1, current_combination + letter)
                backtrack_func(idx + 1, current_combination + letter)

        result = []
        backtrack_func(0, "")

        return result

    def AlternateSolution2(self, digits):
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for letter in digit_to_letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        result = []
        backtrack("", digits)

        return result

sol = Solution()
digits = "23"  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations_OWN(digits))
print(sol.AlternateSolution(digits))

digits = ""  # []
print(sol.letterCombinations_OWN(digits))
print(sol.AlternateSolution(digits))

digits = "2"  # ["a", "b", "c"]
print(sol.letterCombinations_OWN(digits))
print(sol.AlternateSolution(digits))

digits = "234"
print(sol.letterCombinations_OWN(digits))
print(sol.AlternateSolution(digits))