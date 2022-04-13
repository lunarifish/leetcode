# 2022-4-14 1:30:40
# Runtime 36ms(70.1%)
# Memory 15mb(38.3%)

class Solution:
        def maximumWealth(self, accounts: List[List[int]]) -> int:
            ret = 0
            for client in accounts:
                if (cur := sum(client)) > ret:
                    ret = cur
            return ret
