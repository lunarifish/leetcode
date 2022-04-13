// 2022-4-7
// Runtime 16ms(65.7%)
// Memory 16.5mb(28.2%)

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if(nums.size() == 1) return nums[0];
        int ret = nums[0];
        for(int i = 1; i < nums.size(); i++) {
            ret ^= nums[i];
        }
        return ret;
    }
};
