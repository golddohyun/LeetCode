class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        
        if len(s) <= 1 : return s
        if len(set(s)) <= 1 : return s
        
        max_len, max_str = 1, s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                curstr = s[i:j+1]
                if curstr == curstr[::-1] and max_len < len(curstr):
                    max_len = len(curstr)
                    max_str = curstr
        return max_str