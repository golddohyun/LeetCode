class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2 : return len(s)
        curmax= 0
        for i in range(len(s)) :
            ptr = i
            subst = ""
            while ptr < len(s) :
                if s[ptr] in subst :
                    break
                else : 
                    subst+=s[ptr]
                    ptr+=1  
            if len(subst) > curmax : 
                curmax = len(subst)
        return curmax
