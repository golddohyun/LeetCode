class Solution {
public:
    bool is_palindrome(string mystr){
        int start = 0, end = mystr.size()-1;
        while (start < end) {
            if (mystr[start] != mystr[end]) return false;
            start++;
            end--;
        }
        return true;
    }
    
    void backtrack(string s, int start, vector<string> path, vector<vector<string>>& result ){
        if (start == s.size()){
            result.push_back(path);
            return;
        }
        for (int idx=start; idx < s.size(); idx++){
            int end = idx;
            string mysub = s.substr(start, end-start+1);
            if (is_palindrome(mysub)){
                path.push_back(mysub);
                backtrack(s, end+1, path, result);
                path.pop_back();
            }
        }
        
    }
    vector<vector<string>> partition(string s) {
        vector<string> path;
        vector<vector<string>> result;
        backtrack(s, 0, path, result);
        return result;        
    }
};