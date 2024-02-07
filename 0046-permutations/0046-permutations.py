class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        used = [0]*N

        def backtrack_permute(arr, result):
            if len(arr) == N :
                result.append(arr[:])
                return 

            for i in range(N) :
                if not used[i] :
                    arr.append(nums[i])
                    used[i] = 1
                    backtrack_permute(arr, result)
                    used[i] = 0
                    arr.pop()
        result = []
        backtrack_permute([],result)
        return result
