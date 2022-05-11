// 2022-05-11 18:25:34
// Runtime 8ms(71.9%)
// Memory 11.6mb(79.2%)

class Solution {
public:
    bool match(string s, string pre) {
        bool ret = true;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != pre[i]) {
                ret = false;
                break;
            }
        }
        return ret;
    }
    int countPrefixes(vector<string>& words, string s) {
        int ret = 0;
        for (string st : words) {
            if (match(st, s))
                ++ret;
        }
        return ret;
    }
};
