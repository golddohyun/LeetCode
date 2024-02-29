class Solution {
public:
    void backtrackUnique(vector<int>& arr, vector<int>& used, vector<vector<int>>& result, vector<int>& nums, int start){
        if (arr.size() == nums.size()) {
            result.push_back(arr);
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;

            if (!used[i]) {
                used[i] = 1;
                arr.push_back(nums[i]);
                backtrackUnique(arr, used, result, nums, 0);
                used[i] = 0;
                arr.pop_back();
            }
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> arr;
        vector<int> used(nums.size(), 0);
        vector<vector<int>> result;

        backtrackUnique(arr, used, result, nums, 0); 
        return result;        
    }
};
