class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack_comb(start, arr, mx_len) :
            if len(arr) == mx_len :
                result.append(arr)
                return
            for idx in range(start, len(nums)) :
                backtrack_comb(idx+1, arr+[nums[idx]], mx_len)

        result = []
        for k in range(len(nums)+1) :
            backtrack_comb(0, [], k)    
        return result