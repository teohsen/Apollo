class Solution:
    """
    0 0
    1 1
    2 0 + 1 = 1
    3 1 + 1 = 2
    4 1 + 2 = 3
    5 2 + 3 = 5
    """

    def fib(self, n: int) -> int:
        if n == 0 :
            return 0
        if n == 1 :
            return 1

        cache = [0, 1] + [0] * (n - 1)

        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        print(cache[n])
        return cache[n]

    def fib(self, n):
        if n <= 1:
            return n
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a+b

        return a