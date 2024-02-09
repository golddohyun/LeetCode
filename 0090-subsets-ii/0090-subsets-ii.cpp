class Solution {
public:
    void backtrack_comb(int start, int mx_len, const vector<int>& nums, vector<vector<int>>& res, vector<int>& arr) {
        if (arr.size() == mx_len) {
            res.push_back(arr);
            return;
        }
        int prev = -1;
        for (int idx=start; idx < nums.size(); idx++){
            if (idx > start && prev == nums[idx]) continue;
            prev = nums[idx];
            arr.push_back(prev);
            backtrack_comb(idx+1, mx_len, nums, res, arr);
            arr.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums){
        vector<vector<int>> res;
        vector<int> arr;
        sort(nums.begin(), nums.end());
        for (int k=0; k < nums.size()+1; k++){
            backtrack_comb(0, k, nums, res, arr);
        }
        return res;
    }
};


