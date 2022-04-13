# 2022-4-12
# Runtime 40ms(49.7%)
# Memory 15mb(22.1%)

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total = 0
        lines = 1
        a = ord("a")
        for char in s:
            total += widths[ord(char) - a]
            if total > 100:
                total = widths[ord(char) - a]
                lines += 1
        return [lines, total]
