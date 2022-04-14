// 2022-3-30 9:26
// Runtime 4ms(94.9%)
// Memory 5.8mb(62.9%)

class Solution {
public:
    bool isPalindrome(int x) {
        using namespace std;
        int count = 0;
        bool arraysEqual = true;
        string xst = to_string(x);
        char rvs[xst.size()];
        for(int i = 0; i < xst.size(); i++) rvs[xst.size() - 1 - i] = xst[i];
        while (arraysEqual && count < xst.size()) {
            if(xst[count] != rvs[count]) arraysEqual = false;
            count++;
}
        return arraysEqual;
    }
};
