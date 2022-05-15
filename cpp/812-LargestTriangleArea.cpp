// 2022-05-15 16:44:44
// Runtime 4ms(97.2%)
// Memory 7.4mb(69.8%)

class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double ret(-999), cur;
        for (auto it1(points.begin()); it1 != points.end() - 2; ++it1) {
            for (auto it2(it1 + 1); it2 != points.end() - 1; ++it2) {
                for (auto it3(it2 + 1); it3 != points.end(); ++it3) {
        cur = 
        abs((*it1)[0] * (*it2)[1] + 
            (*it2)[0] * (*it3)[1] +
            (*it3)[0] * (*it1)[1] - 
            (*it1)[0] * (*it3)[1] - 
            (*it2)[0] * (*it1)[1] - 
            (*it3)[0] * (*it2)[1]);
                    if (cur > ret)
                        ret = cur;
                }
            }
        }
        return 0.5 * ret;
    }
};
