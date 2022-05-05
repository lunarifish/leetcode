# 2022-05-06 03:05:58
# Runtime 304ms(10.3%)
# Memory 15mb(24.5%)

##
# 简单模拟了一下所以就巨慢
# 感觉应该可以用数学方法解决
###

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(n))
        i = 0
        res = list()
        while len(players) > 1:
            for j in range(k - 1):
                if i >= len(players) - 1:
                    i = 0
                else:
                    i += 1
            players.pop(i)
            if i == len(players):
                i = 0
        return players[0] + 1
