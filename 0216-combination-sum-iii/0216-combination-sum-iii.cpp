class Solution {
public:

    void backtrack_comb(vector<int>& arr, vector<vector<int>>& result, vector<int>& used, int start, int& maxlength, int target){
        if (arr.size() == maxlength && target == 0){
            result.push_back(arr);
            return;
        }
        for (int i=start; i < 10; i++){
            if (used[i]) continue;
            used[i] = 1;
            arr.push_back(i);
            backtrack_comb(arr, result, used, i+1, maxlength, target-i);
            arr.pop_back();
            used[i] = 0;
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> used(10, 0);
        vector<int> arr;
        vector<vector<int>> result;
        backtrack_comb(arr, result, used, 1, k, n);

        return result;
    }
};