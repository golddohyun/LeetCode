class Solution {
public:
    void backtrack_comb(int start, int mx_len, const vector<int>& nums, vector<vector<int>>& res, vector<int>& arr) {
        if (arr.size() == mx_len) {
            res.push_back(arr);
            return;
        }
        for (int idx=start; idx < nums.size(); idx++){
            arr.push_back(nums[idx]);
            backtrack_comb(idx+1, mx_len, nums, res, arr);
            arr.pop_back();
        }

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> arr;
        for (int k=0; k < nums.size()+1; k++){
            backtrack_comb(0, k, nums, res, arr);
        }
        // for (const auto &row : res) {
        //     cout << "[ ";
        //     for (const auto &elem : row) cout << elem << " ";
        //     cout << "], ";
        // }
        return res;
    }
};