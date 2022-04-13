// 2022-3-29 20:46
// Runtime 116ms(27.7%)
// Memory 41.7mb(43.8%)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var find = false;
    for(var i = 0; i < nums.length; i ++) {
        if(find) break;
        for(var j = i + 1; j < nums.length; j++) {
            if(nums[i] + nums[j] == target) {
                var ret = [i, j];
                find = true;
                break;
            }
        }
    }
    return ret;
};
