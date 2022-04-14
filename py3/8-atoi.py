# 2021-12-30 17:12
# Runtime 49ms(10.3%)
# Memory N/A

class Solution:
    def myAtoi(self, s: str) -> int:
        INF_P = 2 ** 31 - 1
        INF_N = -(2 ** 31)
        if len(s) == 0:
            return 0
        s = list(s)
        while s[0] == ' ':
            s.pop(0)
            if len(s) == 0:
                return 0
        negative = False
        if s[0] == '+':
            s.remove('+')
        elif s[0] == '-':
            negative = True
            s.remove('-')
        else: pass
        if len(s) == 0:
            return 0
        num = []
        for i in s:
            try:
                int(i)
            except ValueError:
                break
            else:
                num.append(i)
        if len(num) == 0:
            return 0
        else:
            result = int(''.join(num))
        if negative:
            result = -result
        else: pass
        if result <= INF_P and result >= INF_N:
            return result
        if result < INF_N:
            return INF_N
        else:
            return INF_P
            
