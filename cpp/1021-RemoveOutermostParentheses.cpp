// 2022-05-28 03:12:42
// Runtime 0ms(100.0%)
// Memory 6.9mb(9.7%)

class Solution {
public:
    string removeOuterParentheses(string s) {
        int i, stack_depth = 0;
        string ret = "";
        queue<int> deletes;
        
        for (i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                if (stack_depth == 0)
                    deletes.push(i);
                ++stack_depth;
            } else if (s[i] == ')') {
                if (stack_depth == 1)
                    deletes.push(i);
                --stack_depth;
            }
        }
        for (i = 0; i < s.size(); ++i) {
            if (i == deletes.front()) 
                deletes.pop();
            else
                ret += s[i];
        }
        return ret;
    }
};
