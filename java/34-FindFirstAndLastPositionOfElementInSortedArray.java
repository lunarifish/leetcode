// 2022-04-22 21:35:29
// Runtime 1ms(10.6%)
// Memory 44.2mb(84.4%)

/**
 * 你连二分查找都不会，我为什么要给你机会
 */

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int i;
        int[] ret = {-1, -1};
        boolean find = false;
        for (i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                ret[0] = i;
                find = true;
                break;
            }
        }
        if (!find)
            return ret;
        for(i = i; i < nums.length; i++) {
            if (i == nums.length - 1 || nums[i + 1] != target) {
                ret[1] = i;
                break;
            }
        }
        return ret;
    }
