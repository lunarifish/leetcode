# 2022-01-10 00:21
# Runtime 7028ms(5.0%)
# Memory 470mb(5.0)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        out = []
        for i in range(len(nums))[:-2]:
            l = i + 1
            r = len(nums) - 1
            while l != r:
                lb = nums[l] >= nums[r]
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif cur < 0:
                    if lb: r -= 1
                    else: l += 1
                else:
                    if lb: l += 1
                    else: r -= 1
        for i in range(len(res)):
            res[i].sort()
        for i in res:
            if i not in out:
                out.append(i)
        return out
