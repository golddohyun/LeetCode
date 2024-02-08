class Solution {
public:
    void backtrackComb(int start, int target, vector<int>& candidates, vector<int>& arr, vector<vector<int>>& result){
        if (target == 0 ){
            result.push_back(arr);
            return;
        }
        int prev = -1;
        for (int idx=start; idx < candidates.size(); idx++){
            if (candidates[idx] == prev) continue;
            if (candidates[idx] <= target) {
                prev = candidates[idx];
                arr.push_back(candidates[idx]);
                backtrackComb(idx+1, target-candidates[idx], candidates, arr, result);
                arr.pop_back();
            }
        }

    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> arr;
        // sort candidates
        sort(candidates.begin(), candidates.end(), [](int a, int b){
            return a < b;
        }
        );
        backtrackComb(0, target, candidates, arr, result);
        return result;        
    }
};
