// 2022-04-23 13:29:14
// Runtime 0ms(100.0%)
// Memory 6.9mb(56.8%)

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> aux;
        vector<int> line;
        int i, j;
        for (i = 0; i < matrix[0].size(); ++i) {
            line.clear();
            for (j = matrix.size() - 1; j > -1; --j) {
             line.push_back(matrix[j][i]);
            }
            aux.push_back(line);
        }
        matrix = aux;
    }
};
