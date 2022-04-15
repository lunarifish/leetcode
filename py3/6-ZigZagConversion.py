# 2022-4-16 3:57
# Runtime 52ms(86.0%)
# Memory 15.2mb(38.9%)

##
# 写的实在是太丑了..但是好像意外的有点快
# ??
###

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cycle = numRows * 2 - 2
        lines = [list() for i in range(numRows)]
        upward_index = range(numRows)
        downward_index = range(numRows)[1:-1][::-1]
        index = 0
        try:
            while True:
                for i in upward_index:
                    lines[i].append(s[index])
                    index += 1
                for i in downward_index:
                    lines[i].append(s[index])
                    index += 1
        except IndexError:
            out = list()
            for i in lines:
                out += i
            return "".join(out)
