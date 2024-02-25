class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numstr = str(x)
        return numstr == numstr[::-1]