# 2022-05-11 02:50:54
# Runtime 48ms(23.0%)
# Memory 14.9mb(81.0%)

##
# 这么慢属于是没想到
###
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ret = float("-inf")
        def isGood(s):
            return True if len(set(s)) == 1 else False
        for l in range(len(num) - 2):
            if isGood(num[l:l + 3]):
                if (cur := int(num[l:l + 3])) > ret:
                    ret = cur
        return str(ret).rjust(3, "0") if ret != float("-inf") else ""
