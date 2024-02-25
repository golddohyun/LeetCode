class Solution {
public:
    string reverse(string src){
        string tmp = "";
        for (int i = src.size() - 1; i >= 0; i--) {
            tmp += src[i];
        }
        return tmp;
    }
    
    string intToString(int x) {
        if (x == 0) return "0"; 

        string str;
        bool isNegative = false;

        if (x == INT_MIN) {
            return "-2147483648";
        }

        if (x < 0) {
            isNegative = true; 
            x = -x; 
        }

        while (x > 0) {
            char digit = (x % 10) + '0';
            str = digit + str;
            x /= 10;
        }

        if (isNegative) {
            str = "-" + str;
        }
        return str;
    }

    bool isPalindrome(int x) {
        if (x < 0) return false; 
        string x_str = intToString(x);
        return reverse(x_str) == x_str;
    }
};