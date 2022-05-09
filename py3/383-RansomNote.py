# 2022-05-10 00:03:53
# Runtime 84ms(31.4%)
# Memory 15.1mb(54.3%)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        bank = defaultdict(int)
        for i in magazine:
            bank[i] += 1
        for i in ransomNote:
            if bank[i]:
                bank[i] -= 1
            else:
                return False
        return True


"""---------------------------------------------"""


# 2022-05-10 00:09:46
# Runtime 60ms(68.8%)
# Memory 15.1mb(41.1%)

##
# 参考题解
###

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for i in ransomNote:
            cnt1[i] += 1
        for i in magazine:
            cnt2[i] += 1
        for i in cnt1:
            if cnt1[i] > cnt2[i]:
                return False
        return True
