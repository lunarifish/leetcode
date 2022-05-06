// 2022-05-06 22:54:33
// Runtime 580ms(5.0%)
// Memory 76.8mb(5.0%)

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() < 4)
            return {};
        set<vector<int>> unique;
        vector<vector<int>> ret;
        short it1, it2, l, r;
        long cur;
        std::sort(nums.begin(), nums.end());
        
        for (it1 = 0; it1 <= nums.size() - 4; ++it1) {
            for (it2 = it1 + 1; it2 <= nums.size() - 3; ++it2) {
                l = it2 + 1;
                r = nums.size() - 1;
                while (l < r) {
                    cur = (long)nums[it1] + (long)nums[it2] + (long)nums[l] + (long)nums[r];
                    if (cur > target)
                        --r;
                    else if (cur < target)
                        ++l;
                    else {
                        unique.insert({nums[it1], nums[it2], nums[l], nums[r]});
                        ++l;
                    }
                }
            }
        }
        ret.assign(unique.begin(), unique.end());
        return ret;
    }
};


/*---------------------------------------------*/


// 2022-5-6 23:18
// Runtime 432ms(5.0%)
// Memory 76.6mb(5.0%)

/**
 * 剪枝剪了个寂寞
 */

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() < 4)
            return {};
        set<vector<int>> unique;
        vector<vector<int>> ret;
        short it1, it2, l, r;
        long cur;
        std::sort(nums.begin(), nums.end());
        
        for (it1 = 0; it1 <= nums.size() - 4; ++it1) {
            if ((long)nums[it1] + nums[it1 + 1] + nums[it1 + 2] + nums[it1 + 3] > target)
                break;
            if ((long)nums[it1] + nums[nums.size() - 1] + nums[nums.size() - 2] + nums[nums.size() - 3] < target)
                continue;
            for (it2 = it1 + 1; it2 <= nums.size() - 3; ++it2) {
                if ((long)nums[it1] + nums[it2] + nums[it2 + 1] + nums[it2 + 2] > target)
                    break;
                if ((long)nums[it1] + nums[it2] + nums[nums.size() - 1] + nums[nums.size() - 2] < target)
                    continue;
                l = it2 + 1;
                r = nums.size() - 1;
                while (l < r) {
                    cur = (long)nums[it1] + nums[it2] + nums[l] + nums[r];
                    if (cur > target)
                        --r;
                    else if (cur < target)
                        ++l;
                    else {
                        unique.insert({nums[it1], nums[it2], nums[l], nums[r]});
                        ++l;
                    }
                }
            }
        }
        ret.assign(unique.begin(), unique.end());
        return ret;
    }
};
