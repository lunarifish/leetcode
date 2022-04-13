// 2022-3-29 17:44
// Runtime 50ms(34.5%)
// Memory 41.2mb(67.8%)

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ret = new int[2];
        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    ret[0] = i;
                    ret[1] = j;
                }
            }
        }
        return ret;
    }
}
