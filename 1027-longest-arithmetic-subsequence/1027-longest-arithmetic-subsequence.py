class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        difdict = {}
        maxlen = 0
        for j in range(len(nums)):
            difdict[j] = {}
            for i in range(j):
                diff = nums[j] - nums[i]
                if diff in difdict[i]:
                    difdict[j][diff] = difdict[i][diff] + 1
                else:
                    difdict[j][diff] = 2
                maxlen = max(maxlen, difdict[j][diff])
        return maxlen