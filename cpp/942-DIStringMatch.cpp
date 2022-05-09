// 2022-05-09 17:45:16
// Runtime 4ms(88.5%)
// Memory 8.8mb(28.4%)

class Solution {
public:
    vector<int> diStringMatch(string s) {
        vector<int> ret;
        int min = 0, max = s.size();
        for(char i : s) {
            if (i == 'I') {
                ret.push_back(min);
                ++min;
            } else if (i == 'D') {
                ret.push_back(max);
                --max;
            }
        }
        ret.push_back(max);
        return ret;
    }
};
