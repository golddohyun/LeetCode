class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1] : return 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for left in range(n-1, -1, -1) :
            dp[left][left] = 1
            for right in range(left+1,len(s)) : 
                if s[left] == s[right] :
                    dp[left][right] = 2 + dp[left+1][right-1]
                else :
                    dp[left][right] = max(dp[left][right-1], dp[left+1][right])

        return len(s) - dp[0][len(s)-1]