class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for val in arr :
            former = dp.get(val-difference, 0)
            dp[val] = former+1
        return max(dp.values())