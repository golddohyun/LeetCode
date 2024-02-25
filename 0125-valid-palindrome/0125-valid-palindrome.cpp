class Solution {
public:
    bool isPalindrome(string s) {
        string newstr = "";
        for (auto let : s){
            if ((let >='a' && let <= 'z') || (let >='0' && let <= '9')) {
                newstr+=let;
            }
            else if ((let >='A' && let <= 'Z')) {
                newstr+=let+32;
            }
            else continue;
        }
        // for (auto i : newstr){
        //     cout << i << ' ';
        // }
        // cout << endl;

        // is palindrome check
        int start=0;
        int end= newstr.size() -1;

        while (start < end){
            if (newstr[start] != newstr[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};

