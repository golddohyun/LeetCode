class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # numstr = str(x)
        return str(x) == str(x)[::-1]