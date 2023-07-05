class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums: return 0
        if 0 not in nums: return len(nums)-1

        splist = ''.join(map(str, nums)).split('0')
        mlength = 0
        for i in range(len(splist)-1) :
            subarr = len(splist[i])+ len(splist[i+1])
            if subarr > mlength : mlength = subarr
        return mlength