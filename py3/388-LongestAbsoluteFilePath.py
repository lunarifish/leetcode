# 2022-05-03 22:25:11
# Runtime 36ms(71.0%)
# Memory 14.9mb(82.3%)

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def deserialize(s):
            ret = 0
            while s[ret] == "\t":
                ret += 1
            return s[ret:], ret, "." in s

        ret = 0
        cur = list()
        cur_depth = -1
        for i in [deserialize(i) for i in input.split("\n")]:
            if i[1] > cur_depth:
                cur.append((len(i[0]), i[2]))
                cur_depth += 1
            elif i[1] < cur_depth:
                while cur_depth != i[1]:
                    cur.pop(-1)
                    cur_depth -= 1
                cur[-1] = (len(i[0]), i[2])
            else:
                cur[i[1]] = (len(i[0]), i[2])
            
            if cur[-1][1] and sum([i[0] for i in cur]) + cur_depth > ret:
                ret = sum([i[0] for i in cur]) + cur_depth
        return ret
