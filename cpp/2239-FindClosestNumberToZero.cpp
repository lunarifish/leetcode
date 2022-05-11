// 2022-05-11 19:23:48
// Runtime 20ms(68.0%)
// Memory 19.1mb(54.2%)

/**
 * 庆祝100题
 */

class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int min_delta = 0x7fffffff;
        int ret, cur;
        for (int i : nums) {
            if ((cur = abs(i)) < min_delta) {
                min_delta = cur;
                ret = i;
            } else if (abs(i) == min_delta) {
                if (i > ret)
                    ret = i;
            }
        }
        return ret;
    }
};
