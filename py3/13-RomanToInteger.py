# 2022-01-06 20:53
# Runtime 52ms(56.6%)
# Memory N/A(100.0%)

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        arr = []
        pat = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
        val = [900, 400, 90, 40, 9, 4, 1000, 500, 100, 50, 10, 5, 1]
        for i in pat:
            while s.find(i) != -1:
                arr.append(i)
                s = s.replace(i, '0' * len(i), 1)
        for i in arr:
            sum += val[pat.index(i)]
        return sum
