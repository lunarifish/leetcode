// 2022-05-12 13:47:01
// Runtime 40ms(34.0%)
// Memory 11.8mb(92.7%)

class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int ret = 0;
        for (int i = 0; i < strs[0].size(); ++i) {
            for (int j = 0; j < strs.size() - 1; ++j) {
                if (strs[j][i] > strs[j + 1][i]) {
                    ++ret;
                    break;
                }
            }
        }
        return ret;
    }
};
