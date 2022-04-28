# 2022-01-14 18:58
# Runtime 36ms(78.7%)
# Memory 15.1mb(35.0%)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(min([len(i) for i in strs])):
            fst = strs[0][i]
            for j in strs:
                if j[i] != fst:
                    return res
            res += fst
        return res
