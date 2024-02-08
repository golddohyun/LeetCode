class Solution {
public:
    void backtrack_comb(int start, int target, vector<int>& candidates, vector<int>& arr, vector<vector<int>>& result){
        if (target == 0) {
            result.push_back(arr);
            return;
        }
        for (int idx=start; idx < candidates.size(); idx++) {
            if (candidates[idx] <= target) {
                arr.push_back(candidates[idx]);
                backtrack_comb(idx, target-candidates[idx], candidates, arr, result);
                arr.pop_back();
            }
        }

    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> arr;
        backtrack_comb(0, target, candidates, arr, result);
        return result;
        
    }
};