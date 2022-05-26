// 2022-05-27 02:53:03
// Runtime 92ms(82.6%)
// Memory 57.9mb(90.9%)

class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        vector<int> pos1, pos2;
        int i, j, cur;
        int min_delta = 0x7fffffff;
        for (i = 0; i < words.size(); ++i) {
            if (words[i] == word1)
                pos1.push_back(i);
            else if (words[i] == word2)
                pos2.push_back(i);
            else ;
        }
        i = 0;
        j = 0;
        while (i < pos1.size() && j < pos2.size()) {
            if ((cur = abs(pos2[j] - pos1[i])) < min_delta)
				min_delta = cur;
            if (pos1[i] < pos2[j])
                ++i;
            else if (pos1[i] >= pos2[j])
                ++j;
        }
        return min_delta;
    }
};
