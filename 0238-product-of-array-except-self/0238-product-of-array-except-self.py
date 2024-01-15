# class Solution(object):
#     # Runtime: 161 ms, faster than 81.68%
#     # Memory Usage: 19.2 MB, less than 95.60%
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         num_dict, ans = dict.fromkeys(nums, 0), []
#         for item in nums : num_dict[item] +=1
#         # get total multiplication (except 0)
#         mul = 1
#         for num, m in num_dict.items() :
#             if num != 0 :
#                 mul *= num **m

#         if 0 not in num_dict.keys() :
#             for item in nums :
#                 ans.append(mul//item)
#         else : 
#             if num_dict[0] == 1 :
#                 for item in nums :
#                     if item == 0 :
#                         ans.append(mul)
#                     else :
#                         ans.append(0)
#             if num_dict[0] > 1 :
#                 return [0]*len(nums)
#         return ans

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)

        # get total multiplication (except 0)
        mul, ans = 1, []
        for num in nums:
            if num != 0:
                mul *= num
        for num in nums:
            if zero_count == 0:
                ans.append(mul // num)
            else:
                ans.append(mul if num == 0 else 0)
        return ans
