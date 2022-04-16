# 2022-4-16 12:07
# Runtime 32ms(84.8%)
# Memory 14.9mb(37.9%)

##
# 找了一上午状态转移方程
# 一看题解 f(x)=f(x-1)+f(x-2) 哈哈
###

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        from itertools import permutations
        def findAllSubSets(ones):
            twos = 0
            ret = list()
            while ones >= 0:
                cur = [1] * ones + [2] * twos
                ret += list(permutations(cur))
                ones -= 2
                twos += 1
            return list(set(ret))
        
        previous = []
        for i in range(1, n + 1):
            if len(previous) < 2:
                previous.append(len(findAllSubSets(i)))
            else:
                previous.append(sum(previous))
                previous = previous[1:]
        return previous[1]
