class Solution {
public:
   bool isPalindrome(string str) {
    int left = 0, right = str.length() - 1;
    while (left < right) {
        if (str[left++] != str[right--])
            return false;
    }
    return true;
}

void partitionUtil(vector<vector<string>> &res, vector<string> &curr, 
                   int start, string str) {
    if (start == str.length()) {
        res.push_back(curr);
        return;
    }
    for (int i = start; i < str.length(); i++) {
        if (isPalindrome(str.substr(start, i - start + 1))) {
            curr.push_back(str.substr(start, i - start + 1));
            partitionUtil(res, curr, i + 1, str);
            curr.pop_back();
        }
    }
}

vector<vector<string>> partition(string str){
    vector<vector<string>> res;
    vector<string> curr;
    partitionUtil(res, curr, 0, str);
    return res;
}

};