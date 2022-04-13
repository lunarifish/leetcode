// 2022-3-29 20:38
// Runtime 160ms(53.5%)
// Memory 43mb(63.3%)

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] ret = new int[2];
        bool find = false;
        for(int i = 0; i < nums.Length; i = i + 1) {
            if(find) break;
            for(int j = i + 1; j < nums.Length; j = j + 1) {
                if(nums[i] + nums[j] == target) {
                    ret[0] = i;
                    ret[1] = j;
                    find = true;
                    break;
                }
            }
        }
        return ret;
    }
}
