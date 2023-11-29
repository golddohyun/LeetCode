class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        
        def is_palindrome(s):
            start, end = 0, len(s)-1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        for i in words:
            if is_palindrome(i):
                return i
        return ""