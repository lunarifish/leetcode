# 2022-05-14 21:33:19
# Runtime 44ms(60.9%)
# Memory 15mb(9.7%)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        l, r = 0, x
        while l + 1 < r:
            m = (l + r) // 2
            if m * m <= x:
                l = m
            else:
                r = m
        return l
