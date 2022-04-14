# 2022-1-10 00:48
# Runtime 6856ms(32.4%)
# Memory 15.2mb(58.4%)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(1, len(s) + 1)[::-1]:
            for j in range(len(s) - i + 1):
                if s[j:j + i] == s[j:j + i][::-1]:
                    return s[j:j + i]
