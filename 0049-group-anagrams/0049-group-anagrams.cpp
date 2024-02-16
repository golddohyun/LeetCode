class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> str_dict;
        for (auto s : strs) {
            string tmp = s;
            sort(tmp.begin(), tmp.end());
            str_dict[tmp].push_back(s);
        }
        vector<vector<string>> ans;
        for (auto elem : str_dict) {
            ans.push_back(elem.second);
        }
        return ans;
    }
};