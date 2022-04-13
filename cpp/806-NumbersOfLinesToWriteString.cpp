// 2022-4-12
// Runtime 0ms(100.0%)
// Memory 6.5mb(96.2%)

/**
 * 96.2%啊啊啊啊啊啊啊啊啊啊100%啊啊啊啊啊啊
 */

class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines(1), row(0);
        for(int i(0); i < s.size(); i++) {
            row += widths[s[i] - 'a'];
            if(row > 100) {
                ++lines;
                row = widths[s[i] - 'a'];
            }
        }
        return {lines, row};
    }
};
