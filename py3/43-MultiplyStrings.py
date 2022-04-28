# 2022-04-29 03:29:27
# Runtime 44ms(76.4%)
# Memory 15.1mb(32.5%)

##
# 虽然就是说好像有点不符合题意
###

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = 0
        for digit, i in enumerate(num2[::-1]):
            ret += int(num1) * int(i) * (10 ** digit)
        return str(ret)
