# 2022-4-16 4:52
# Runtime 96ms(96.8%)
# Memory 26.3mb(11.9%)

##
# 好像学会dp了
###

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findMaxFrom(l):
            ret = float("-inf")
            cur = 0
            for i in l:
                cur += i
                if cur > ret:
                    ret = cur
            return ret
        
        previous = None
        ret = float("-inf")
        for i in range(len(nums))[::-1]:
            if previous is None:
                previous = findMaxFrom(nums[i:])
            else:
                if previous > 0:
                    previous += nums[i]
                else:
                    previous = nums[i]
            if previous > ret:
                ret = previous
        return ret
