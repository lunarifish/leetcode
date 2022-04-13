// 2022-4-12
// Runtime 148ms(33.7%)
// Memory 41.5mb(36.0%)

public class Solution {
    public int[] NumberOfLines(int[] widths, string s) {
        int lines = 1, row = 0;
        int[] ret = new int[2];
        for(int i = 0; i < s.Length; i++) {
            row += widths[s[i] - 'a'];
            if(row > 100) {
                lines++;
                row = widths[s[i] - 'a'];
            }
        }
        ret[0] = lines;
        ret[1] = row;
        return ret;

    }
}
