// 2022-05-15 17:55:04
// Runtime 8ms(58.3%)
// Memory 13.9mb(5.2%)

/**
 * 二分查找是吧 现在会了
 */

class Solution {
public:
    int binarySearch(vector<int> arr, int target, bool upper) {
        int l(-1), r(arr.size()), m;
        if (upper) {
            while (l + 1 != r) {
                m = (l + r) / 2;
                if (arr[m] <= target)
                    l = m;
                else
                    r = m;
            }
            return l;
        }
        else {
            while (l + 1 != r) {
                m = (l + r) / 2;
                if (arr[m] < target)
                    l = m;
                else
                    r = m;
            }
            return r;
        }
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        if (!nums.size())
            return {-1, -1};
        
        int upper, lower;
        upper = binarySearch(nums, target, true);
        lower = binarySearch(nums, target, false);
        if (upper < 0)
            upper = 0;
        
        if (nums[upper] != target ||
            nums[lower] != target)
            return {-1, -1};
        else
            return {lower, upper};
    }
};
