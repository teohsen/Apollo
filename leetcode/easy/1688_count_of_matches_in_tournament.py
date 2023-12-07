class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 1

        total_matches = 0
        while n != 2:
            num_of_matches = n // 2
            n = num_of_matches + n % 2
            total_matches += num_of_matches

        return total_matches + 1
