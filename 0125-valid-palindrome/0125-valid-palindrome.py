## valid palindrome 1
class Solution(object):
    def isPalindrome(self, s):
        def palindrome(st) :
            start, end= 0, len(st)-1
            while start < end :
                if st[start] != st[end] : return False
                start+=1
                end-=1
            return True
        
        s = s.lower()

        for i in s:
            if False == i.isalnum():
                s = s.replace(i,"")
				# 다른 방법 : s = ''.join(i for i in s if i.isalnum()).lower()

        # def palindrome(s):
        #     idx = len(s)
        #     if(idx%2): # odd number
        #         if s[0:idx//2] == s[idx:idx//2:-1]:
        #             return True
        #     else:
        #         if s[0:idx//2] == s[idx:idx//2-1:-1]:
        #             return True
        #     return False


        return palindrome(s)