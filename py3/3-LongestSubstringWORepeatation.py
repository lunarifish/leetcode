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
 

 """---------------------------------------------"""


# 2022-4-16 2:36
# Runtime 444ms(10.4%)
# Memory 15.2mb(28.1%)

##
# 用滑动窗口再写了一遍
###

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def checkUnique(s):
            exist = set()
            for i in s:
                if i not in exist:
                    exist.add(i)
                else:
                    return False
            return True
        l, r = 0, 0
        ret = 0
        while r <= len(s):
            if checkUnique(s[l:r]):
                r += 1
            else:
                l += 1
            if r - l > ret:
                ret = r - l
        return ret - 1
                
