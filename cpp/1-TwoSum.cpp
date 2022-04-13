// 2022-3-29 20:16
// Runtime 300ms(30.1%)
// Memory 9.7mb(98.1%)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        bool find = false;
        for(int i = 0; i < nums.size(); i++) {
            if(find) break;
            for(int j = i + 1; j < nums.size(); j++) {
                if(nums[i] + nums[j] == target) {
                    ret = {i, j};
                    find = true;
                    break;
                }
            }
        }
        return ret;
    }
};
