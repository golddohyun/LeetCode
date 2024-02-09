class Solution:
    def subsetsWithDup(self, nums) :
        def backtrack_comb(start, arr, mx_len) :
            if len(arr) == mx_len :
                result.append(arr)
                print(result)
                return
            prev = -1
            for idx in range(start, len(nums)) :
                if (idx > start and prev == nums[idx]) : continue
                prev = nums[idx]
                backtrack_comb(idx+1, arr+[nums[idx]], mx_len)
        
        result = []
        nums.sort()
        for k in range(len(nums)+1) :
            backtrack_comb(0, [], k)
        return sorted(result)
