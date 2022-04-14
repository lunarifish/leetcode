# 2021-12-29 19:05
# Runtime 56ms(86.5%)
# Memory N/A

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
