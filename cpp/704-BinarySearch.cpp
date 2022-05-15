// 2022-05-15 16:18:41
// Runtime 20ms(98.4%)
// Memory 27mb(5.6%)

/**
 * 二分查找是吧
 */

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l(-1), r(nums.size()), m;
        while (l + 1 != r) {
            m = (l + r) / 2;
            if (nums[m] == target) {
                l = m;
                break;
            }
            else if (nums[m] < target)
                l = m;
            else
                r = m;
        }
        if (l < 0)
            l = 0;
        
        if (nums[l] == target)
            return l;
        else
            return -1;
    }
};
