# 2022-05-11 17:43:04
# Runtime 40ms(68.4%)
# Memory 15.1mb(91.2%)

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        ret = list()
        for l in nums:
            for i in l:
                counts[i] += 1
        for i in counts:
            if counts[i] == len(nums):
                ret.append(i)
        return sorted(ret)
