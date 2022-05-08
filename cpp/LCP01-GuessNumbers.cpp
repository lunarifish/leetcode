// 2022-05-08 16:44:31
// Runtime 0ms(100.0%)
// Memory 6.2mb(20.9%)

/**
 * ???
 */

class Solution {
public:
    int game(vector<int>& guess, vector<int>& answer) {
        int ret = 0;
        for (int i = 0; i < guess.size(); ++i) {
            if (guess[i] == answer[i])
                ++ret;
        }
        return ret;
    }
};
