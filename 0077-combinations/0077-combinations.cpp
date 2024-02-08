class Solution {
public:
    void backtrack_comb(int start, vector<int>& arr, vector<vector<int>>& result, const int n, const int k) {
        if (arr.size() == k) {
            result.push_back(arr);
            return;
        }
        for (int i=start; i < n+1; i++) {
            arr.push_back(i);
            backtrack_comb(i+1, arr, result, n, k);
            arr.pop_back();
        }

    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> arr;
        backtrack_comb(1, arr, result, n, k);
        return result;        
    }
};