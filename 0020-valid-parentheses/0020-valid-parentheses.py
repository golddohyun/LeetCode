class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystack = []
        for i in s :
            if i in "({[" :
                mystack.append(i)
            else :
                if not mystack or (i == ')' and mystack[-1] != '(') or (i == ']' and mystack[-1] != '[') or (i == '}' and mystack[-1] != '{') :
                    return False
                else :
                    mystack.pop()
        if mystack :
            return False
        else :
            return True  