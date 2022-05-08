// 2022-05-08 16:10:41
// Runtime 96ms(6.8%)
// Memory 43.6mb(6.5)

/**
 * 慢
 */

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ret;
        unordered_set<int> scanned;
        for(int i : nums) {
            if (scanned.find(i) != scanned.end())
                ret.push_back(i);
            scanned.insert(i);
        }
        return ret;
    }
};
