# 2021-12-29 15:19
# Runtime 28ms(98.0%)
# Memory N/A

class Solution:
    def reverse(self, x: int) -> int:
        INF_P = 2 ** 31 - 1
        INF_N = -(2 ** 31)
        negative = False
        result = 0
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            negative = True
        a = range(len(x))
        a = sorted(a, reverse = True)
        for i in a:
            result += int(x[i]) * (10 ** i)
        if result > INF_P or result < INF_N: return 0
        elif negative: return -result
        else: return result
