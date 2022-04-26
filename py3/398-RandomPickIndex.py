# 2022-04-26 17:11:39
# Runtime 136ms(5.8%) 
# Memory 25.6mb(16.2%)

class Solution:
    import random
    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for index, i in enumerate(nums):
            self.map[i].append(index)
    def pick(self, target: int) -> int:
        random.shuffle(self.map[target])
        return self.map[target][0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
