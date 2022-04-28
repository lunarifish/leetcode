# 2022-04-28 22:29:41
# Runtime 40ms(75.7%) 
# Memory 15.1mb(36.1%)

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        front, side, top = 0, 0, 0
        for i in [[i[j] for i in grid] for j in range(len(grid[0]))]:
            front += max(i)
        for i in grid:
            side += max(i)
        for i in [i[j] for i in grid for j in range(len(i))]:
            if i:
                top += 1
                
        return sum((front, side, top))
