// 2022-05-14 21:32:30
// Runtime 0ms(100.0%)
// Memory 5.8mb(49.7%)

class Solution {
public:
    int mySqrt(int x) {
        if (x == 1)
            return 1;
        else {
            int l(0), r(x), m;
            while (l + 1 < r) {
                m = (l + r) / 2;
                if ((long)m * m <= x)
                    l = m;
                else
                    r = m;
            }
            return l;
        }
    }
};
