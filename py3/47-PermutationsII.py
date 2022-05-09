# 2022-05-09 18:18:04
# Runtime 68ms(29.9%)
# Memory 14.8mb(100.0%)

##
# 我顺从了
###

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(set(permutations(nums)))
