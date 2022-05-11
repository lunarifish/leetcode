# 2022-05-11 13:36:03
# Runtime 44ms(16.9%)
# Memory 14.9mb(82.4%)

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ret = 0
        for index, i in enumerate(number):
            if i == digit:
                if (cur := int(number[0:index] + number[index+1:])) > ret:
                    ret = cur
        return str(ret)
