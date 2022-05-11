# 2022-05-12 02:52:28
# Runtime 184ms(15.8%)
# Memory 16.3mb(6.0%)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def isUpward(s):
            for i in range(len(s) - 1):
                if ord(s[i]) > ord(s[i + 1]):
                    return False
            return True
        
        ret = 0
        for i in [[i[j] for i in strs] for j in range(len(strs[0]))]:
            if not isUpward(i):
                ret += 1
        return ret
