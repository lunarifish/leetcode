# 2022-04-19 22:02:10
# Runtime 152ms(5.1%) 
# Memory 15.1mb(33.9%)

##
# to wish upon a probe
###

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def sendProbe(s, target, pos):
            ret = float("inf")
            for index, i in enumerate(s[pos:]):
                if i == target:
                    ret = index
                    break
            for index, i in enumerate(reversed(s[:(pos + 1)])):
                if i == target:
                    if index < ret:
                        ret = index
                        break
            return ret

        ret = list()
        for i in range(len(s)):
            ret.append(sendProbe(s, c, i))
        return ret


"""---------------------------------------------"""


# 2022-04-19 22:08
# Runtime 136ms(5.1%)
# Memory 14.9mb(83.0%)

##
# 嗯嗯我是推导式单推人
###

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def sendProbe(s, target, pos):
            ret = float("inf")
            for index, i in enumerate(s[pos:]):
                if i == target:
                    ret = index
                    break
            for index, i in enumerate(reversed(s[:(pos + 1)])):
                if i == target:
                    if index < ret:
                        ret = index
                        break
            return ret

        return [sendProbe(s, c, i) for i in range(len(s))]
