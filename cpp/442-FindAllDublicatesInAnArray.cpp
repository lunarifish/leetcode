// 2022-05-08 16:10:41
// Runtime 96ms(6.8%)
// Memory 43.6mb(6.5)

/**
 * 慢
 */

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ret;
        unordered_set<int> scanned;
        for(int i : nums) {
            if (scanned.find(i) != scanned.end())
                ret.push_back(i);
            scanned.insert(i);
        }
        return ret;
    }
};


/*---------------------------------------------*/


// 2022-5-8 16:31
// Runtime 36ms(93.7%)
// Memory 32.7mb(70.6%)

/**
 * 题解
 * 那个while循环的作用是什么 我不理解
 * swap只是把两个元素来回换吧
 */

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int i;
        vector<int> ret;
        for(i = 0; i < nums.size(); ++i) {
            while (nums[i] != nums[nums[i] - 1])
                swap(nums[i], nums[nums[i] - 1]);
        }
        for(i = 0; i < nums.size(); ++i) {
            if (i != nums[i] - 1)
                ret.push_back(nums[i]);
        }
        return ret;
    }
};
