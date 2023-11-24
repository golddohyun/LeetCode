class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = s.lower()
        for i in s:
            if False == i.isalnum():
                s = s.replace(i,"")

        def palindorme(s):
            idx = len(s)
            if(idx%2): # odd number
                if s[0:idx//2] == s[idx:idx//2:-1]:
                    return True
            else:
                if s[0:idx//2] == s[idx:idx//2-1:-1]:
                    return True
            return False

        return palindorme(s)