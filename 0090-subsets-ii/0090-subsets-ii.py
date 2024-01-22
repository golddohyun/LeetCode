class Solution:
    # def backtrack_comb(self, nums, idx, k, used, arr, result):
    #     if len(arr)==k and arr not in result:
    #         result.append(arr)
    #     for i in range(idx+1, len(nums)):
    #         if used[i]==False:
    #             used[i] = True
    #             self.backtrack_comb(nums, i, k, used, arr+[nums[i]], result)
    #             used[i] = False
    #     return result

    def backtrack_comb(self, nums, idx, k, used, arr, result):
        if len(arr) == k and arr not in result:
            result.append(arr.copy()) 
        for i in range(idx, len(nums)):
            if not used[i]:
                used[i] = True
                arr.append(nums[i])
                self.backtrack_comb(nums, i+1, k, used, arr, result)
                arr.pop() 
                used[i] = False
        return result

    def subsetsWithDup(self, nums) :
        leng = []
        used = [False for i in range(len(nums))]
        for k in range(len(nums)+1) :
            for elem in self.backtrack_comb(nums, 0, k, used, [], []) :
                elem.sort()
                if elem not in leng :
                    leng.append(elem)

        return leng

        return leng