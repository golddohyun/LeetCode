class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack_comb(nums, idx, k, arr, result, curmax):
            if len(arr) == k :
                result.add(tuple(arr[:]))
                return
            for i in range(idx, len(nums)):
                if nums[i] >= curmax:
                    arr.append(nums[i])
                    backtrack_comb(nums, i+1, k, arr, result, nums[i])
                    arr.pop()
            return list(result)

        ans = [] 
        for k in range(2, len(nums)+1) :
            result = set()
            ans+= backtrack_comb(nums, 0, k, [], result, float('-inf'))

        return [list(i) for i in ans]