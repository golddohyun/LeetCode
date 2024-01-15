class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_dict, ans = dict.fromkeys(nums, 0), []
        for item in nums : num_dict[item] +=1
        # get total multiplication (except 0)
        mul = 1
        for num, m in num_dict.items() :
            if num != 0 :
                mul *= num **m

        if 0 not in num_dict.keys() :
            for item in nums :
                ans.append(mul//item)
        else : 
            if num_dict[0] == 1 :
                for item in nums :
                    if item == 0 :
                        ans.append(mul)
                    else :
                        ans.append(0)
            if num_dict[0] > 1 :
                return [0]*len(nums)
        return ans