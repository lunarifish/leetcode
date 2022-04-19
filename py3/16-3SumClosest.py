# 2022-04-19 22:55:09
# Runtime 224ms(48.4%)
# Memory 15mb(81.1%)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = float("inf")
        delta_min = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                delta = abs(res - target)
                if delta == 0:
                    return res
                if delta < delta_min:
                    delta_min = delta
                    ret = res
                if res > target:
                    if nums[l] > nums[r]:
                        l += 1
                    else:
                        r -= 1
                else:
                    if nums[l] > nums[r]:
                        r -= 1
                    else:
                        l += 1
        return ret
