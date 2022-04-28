# 2022-03-05 12:03
# Runtime 240ms(67.3%)
# Memory 23.4mb(50.3%)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ma = 0
        for i in prices:
            mi = min(mi, i)
            ma = max(ma, i - mi)
        return ma
