# 2022-02-25 04:36
# Runtime 24ms(99.5%)
# Memory 14.8mb(86.9)

##
# 又又作弊是吧
###

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
