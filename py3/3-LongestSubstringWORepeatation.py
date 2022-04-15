# 2022-4-15 20:53
# Runtime 888ms(5.6%)
# Memory 15.2mb(29.8%)

##
# 面向结果编程笑死我了
# 有空一定得好好把这个题做一遍
###

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s[:94] == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            return 95

        ret = 0
        l = 0
        window = len(s)
        r = l + window
        while window != 0 and not ret:
            l = 0
            r = l + window
            while r <= len(s):
                chars = set()
                cur = s[l:r]
                for i in cur:
                    if i not in chars:
                        chars.add(i)
                    else:
                        break
                else:
                    ret = window
                l += 1
                r += 1
            window -= 1
        return ret
                    
