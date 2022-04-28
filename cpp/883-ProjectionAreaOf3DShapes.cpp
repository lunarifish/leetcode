// 2022-04-28 22:42:59
// Runtime 8ms(53.1%)
// Memory 9mb(72.6%)

class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        short front(0), side(0), top(0), i, j, max;
        for (i = 0; i < grid[0].size(); ++i) {
            max = 0;
            for (j = 0; j < grid.size(); ++j) {
                if (grid[j][i] > max)
                    max = grid[j][i];
            }
            front += max;
        }
        for (auto itline(grid.begin()); itline != grid.end(); ++itline) {
            max = 0;
            for (auto it((*itline).begin()); it != (*itline).end(); ++it) {
                if (*it > max)
                    max = *it;
            }
            side += max;
        }
        for (auto itline(grid.begin()); itline != grid.end(); ++itline) {
            for (auto it((*itline).begin()); it != (*itline).end(); ++it) {
                if (*it)
                    side += 1;
            }
        }
        return front + side + top;
    }
};
