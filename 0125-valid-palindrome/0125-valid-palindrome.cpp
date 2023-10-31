class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int i=0, j=n-1;

        while (i<j)
            if (!isAlphaN(s[i])) i++;
            else if (!isAlphaN(s[j])) j--;
            else if (tolower(s[i++]) != tolower(s[j--])) return false;

        return true;
    }

    bool isAlphaN(char x) {
        if (x >= '0' and x <= '9') return true;
        if (x >= 'A' and x <= 'Z') return true;
        if (x >= 'a' and x <= 'z') return true;
        return false;
    }
};