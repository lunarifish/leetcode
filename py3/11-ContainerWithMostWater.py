# 2021-12-31 20:17
# Runtime 846ms(5.1%)
# Memory N/A(100.0%)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        l = 0
        r = len(height) - 1
        while r != l:
            goright = height[l] <= height[r]
            if goright:
                cur = (r - l) * height[l]
            else:
                cur = (r - l) * height[r]
            if cur > max:
                max = cur
            if goright: l += 1
            else: r -= 1
        return max
