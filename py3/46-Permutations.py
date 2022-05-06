# 2022-05-06 23:50:39
# Runtime 36ms(83.3%)
# Memory 14.9mb(98.9%)

##
# 崩不住了
###

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))
