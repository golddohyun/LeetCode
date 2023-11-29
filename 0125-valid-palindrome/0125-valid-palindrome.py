## valid palindrome 1
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        for i in s:
            if False == i.isalnum():
                s = s.replace(i,"")
				# 다른 방법 : s = ''.join(i for i in s if i.isalnum()).lower()
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