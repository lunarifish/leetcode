# 2022-04-20 20:59:27
# Runtime 40ms(53.5%)
# Memory 14.9mb(72.5%)

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def splitLen(s, length):
            ret = list()
            buffer = ""
            for index, i in enumerate(s):
                if index == len(s) - 1:
                    buffer += i
                    ret.append(buffer)
                    break
                buffer += i
                if len(buffer) == length:
                    ret.append(buffer)
                    buffer = ""
            return ret
        while len(s) > k:
            s = "".join([str(m) for m in [sum([int(j) for j in i]) for i in splitLen(s, k)]])
        return s
