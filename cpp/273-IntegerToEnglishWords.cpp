// 2022-05-27 10:48:59
// Runtime 8ms(13.9%)
// Memory 8.4mb(5.1%)

class Solution {
public:
    vector<string> numbers = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    vector<string> ten_ones = {"", "", "", "", "", "", "", "", "", "", "", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    vector<string> segments = {"", "Thousand", "Million", "Billion"};
    
    
    vector<int> splitDigits(int num, int length, bool reversed) {
        vector<int> ret;
        while (num) {
            ret.push_back(num % (int)pow(10, length));
            num /= (int)pow(10, length);
        }
        if (!reversed)
            reverse(ret.begin(), ret.end());
        return ret;
    }
    
    
    string strJoin(vector<string> words) {
        string ret = "";
        if (words.size() == 0)
            return ret;
 
        auto it = words.begin();
        ret += *it;
    
        for (++it; it != words.end(); ++it) {
            if (*it != "") {
                ret += " ";
                ret += *it;
            }
        }
        return ret;
    }
    
    
    vector<string> convert3Digits(int num) {
        vector<string> ret;
        vector<int> digits = splitDigits(num, 1, false);
        int ten(1), one(2);
        
        if (digits.size() == 1) {
            if (numbers[num] != "")
                return {numbers[num]};
            else
                return ret;
        }
        if (digits.size() == 3) {
            ret.push_back(numbers[digits[0]]);
            ret.push_back("Hundred");
        }
        if (digits.size() == 2) {
            --ten;
            --one;
        }
        
        if (digits[ten] != 0) {
            if (digits[one] == 0)
                ret.push_back(tens[digits[ten]]);
            else if (digits[ten] == 1 && digits[one] != 0)
                ret.push_back(ten_ones[digits[ten] * 10 + digits[one]]);
            else {
                ret.push_back(tens[digits[ten]]);
                ret.push_back(numbers[digits[one]]);
            }
        } else
            ret.push_back(numbers[digits[one]]);
        return ret;
    }
    
    
    string numberToWords(int num) {
        if (num == 0)
            return "Zero";
        
        vector<string> words;
        vector<int> parts = splitDigits(num, 3, true);
        
        for (int i = parts.size() - 1; i > -1; --i) {
            if (parts[i]) {
                vector<string> cur = convert3Digits(parts[i]);
                words.insert(words.end(), cur.begin(), cur.end());
                words.push_back(segments[i]);
            }
        }
        
        return strJoin(words);
    }
};
