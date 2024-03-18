// 2023-03-26 16:44:19
// Runtime 8ms(24.21%)
// Memory 7.5mb(50.79%)

/**
 * 男人我回来了
 */

class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        unordered_map<int, bool> map;
        int sum;
        for (auto ptr = nums.begin(); ptr != nums.end() - 1; ptr++) {
            sum = *ptr + *(ptr + 1);
            if (map.find(sum) == map.end())
                map[sum] = true;
            else
                return true;
        }
        return false;
    }
};