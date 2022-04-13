# 2022-4-7
# Runtime 1056ms(11.6%)
# Memory 16.9mb(28.5%)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        save = list()
        for i in nums:
            if i in save: save.remove(i)
            else: save.append(i)
        return save[0]
