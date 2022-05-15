# 2022-05-15 17:31:42
# Runtime 344ms(38.6%)
# Memory 16.5mb(79.0%)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = list()
        def backtrack(st, dst, k, buffer=list(), depth=0):
            if depth == k:
                ret.append(buffer)
                return
            else:
                for i in range(st, dst + 1):
                    backtrack(i + 1, dst, k, buffer+[i], depth+1)
        backtrack(1, n, k)
        return ret
