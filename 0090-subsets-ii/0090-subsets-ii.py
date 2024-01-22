class Solution:
    def backtrack_comb(self, nums, idx, k, used, arr, result):
        if len(arr)==k and arr not in arr:
            result.append(arr)
        for i in range(idx+1, len(nums)):
            if used[i]==False:
                used[i] = True
                self.backtrack_comb(nums, i, k, used, arr+[nums[i]], result)
                used[i] = False
        return result

    def subsetsWithDup(self, nums) :
        leng = []
        used = [False for i in range(len(nums))]
        for k in range(len(nums)+1) :
            for elem in self.backtrack_comb(nums, -1, k, used, [], []) :
                elem.sort()
                if elem not in leng :
                    leng.append(elem)

        return leng