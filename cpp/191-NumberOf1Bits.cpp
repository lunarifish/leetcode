// 2022-06-25 16:25:54
// Runtime 0ms(100.0%)
// Memory 5.8mb(67.2%)

class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t checker = 1;
        int ret = 0;
        for (int i = 0; i < 32; ++i) {
            if (checker & n)
                ++ret;
            checker = checker << 1;
        }
        return ret;
    }
};
