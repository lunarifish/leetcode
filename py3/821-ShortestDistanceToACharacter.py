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
