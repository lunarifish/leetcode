# 2022-01-14 17:38
# Runtime 1152ms(8.1%)
# Memory 15.7mb(99.2%)

##
# 又作弊是吧
###

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                for j in range(nums.count(i) - 1):
                    nums.remove(i)
        return len(nums)
