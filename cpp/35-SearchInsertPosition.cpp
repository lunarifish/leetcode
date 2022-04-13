// 2022-3-30
// Runtime 0ms(100.0%)
// Memory 9.5mb(19.9%)

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int ret;
        if(target < nums[0]) return 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == target) {
                ret = i;
                break;
            }
            if(i == nums.size() - 1) {
                ret = i + 1;
                break;
            }
            if(nums[i] < target && nums[i + 1] > target) {
                ret = i + 1;
                break;
            }
        }
        return ret;
    }
};
