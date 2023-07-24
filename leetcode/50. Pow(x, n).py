class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Sol 1
        return x ** n

        # Sol 2
        # Binary Exponentiation
        def powpow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            result = powpow(x, n // 2)
            if n % 2:
                return result * result * x
            else:
                return result * result

        result = powpow(x, abs(n))
        if n >= 0:
            return result
        else:
            return 1 / result