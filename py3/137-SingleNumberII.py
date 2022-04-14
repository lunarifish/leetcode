# 2022-4-14 12:24
# Runtime 44ms(58.1%)
# Memory 16.3mb(25.5%)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        e = {}
        for i in nums:
            if not i in e:
                e[i] = 1
            else:
                e[i] += 1
        for i in e:
            if e[i] == 1:
                return i
