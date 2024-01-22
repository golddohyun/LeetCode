#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;


class Solution {
public:
    bool isUnique(const vector<int>& arr, const vector<vector<int>>& result) {
        for (const auto& res : result) {
            if (arr == res) {
                return false;
            }
        }
        return true;
    }

    vector<vector<int>> backtrack_comb(vector<int> &nums, int idx, int k, vector<bool> &used, vector<int> &arr, vector<vector<int>> &result){
        if (arr.size() == k) {
            if (isUnique(arr, result)) {
                result.push_back(arr);
                }
        }
        for (int i = idx; i < nums.size(); ++i) {
            if (used[i] == false) {
                used[i] = true;
                arr.push_back(nums[i]);
                backtrack_comb(nums, i + 1, k, used, arr, result);
                arr.pop_back(); // Remove the last element to backtrack
                used[i] = false;
            }
        }
        return result;

    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> leng;
        vector<bool> used(nums.size(), false);
        vector<vector<int>> tempResult;

        for (int k = 0; k <= nums.size(); ++k) {
            tempResult.clear();
            vector<int> arr;
            backtrack_comb(nums, 0, k, used, arr, tempResult);
            for (auto& elem : tempResult) {
                sort(elem.begin(), elem.end());
                if (find(leng.begin(), leng.end(), elem) == leng.end()) {
                    leng.push_back(elem);
                }
            }
        }
        return leng;

        
    }
};