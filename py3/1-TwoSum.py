# 2021-12-29 13:08
# Runtime 4032ms(6.8%)
# Memory N/A

##
# 开局两个for,_________
###

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexer = range(len(nums))
        for i in indexer:
            for j in indexer[(i + 1):]:
                if nums[i] + nums[j] == target: return [i, j]


"""---------------------------------------------"""


# 2022-1-8 20:44
# Runtime 36ms(87.1%)
# Memory 16.2mb(7.6%)

##
# 双指针
###

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = sorted(zip(nums, [i for i in range(len(nums))]), key = lambda s:s[0])
        l = 0
        r = len(nums) - 1
        while l != r:
            sum = mapper[l][0] + mapper[r][0]
            lb = mapper[l][0] > mapper[r][0]
            if sum == target:
                return [mapper[l][1], mapper[r][1]]
            elif sum > target:
                if lb: l += 1
                else: r -= 1
            elif sum < target:
                if lb: r -= 1
                else: l += 1
