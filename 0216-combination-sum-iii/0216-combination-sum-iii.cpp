class Solution {
public:
    void backtrack_comb(int start, const int& k, int target, vector<int>& arr, vector<vector<int>>& res){
        if (arr.size() == k && target == 0) {
            res.push_back(arr);
            return;
        }
        for (int num=start; num < 10; num++){
            if (num <= target){
                arr.push_back(num);
                backtrack_comb(num+1, k, target-num, arr, res);
                arr.pop_back();
            }
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> arr;
        backtrack_comb(1, k, n, arr, res);
        return res;
    }
};

