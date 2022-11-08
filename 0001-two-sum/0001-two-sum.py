class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i]+nums[j] : 
                    ans.append(i)
                    ans.append(j)
        return ans