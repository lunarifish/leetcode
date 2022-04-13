// 2022-4-14 1:38:55
// Runtime 4ms(89.0%)
// Memory 7.6mb(54.9%)

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max(0), current;
        for(int i(0); i < accounts.size(); i++) {
            current = 0;
            for(int j(0); j < accounts[i].size(); j++) 
                current += accounts[i][j];
            if(current > max)
                max = current;
        }
        return max;
    }
};
