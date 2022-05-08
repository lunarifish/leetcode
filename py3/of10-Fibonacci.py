# 2022-05-08 17:22:25
# Runtime 32ms(88.9%)
# Memory 14.8mb(88.3%)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b, c = 0, 1, 1
        for i in range(n - 2):
            a, b, c = b, c, b + c
        return c % 1000000007
