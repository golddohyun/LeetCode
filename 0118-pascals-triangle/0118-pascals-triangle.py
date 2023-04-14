from math import factorial

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def print_factorial(num):
            ls = []
            for j in range(num+1) :
                ls.append(factorial(num)//(factorial(j)*factorial(num-j)))
            return ls
        
        ans = []
        for i in range(numRows) :
            ans.append(print_factorial(i))

        return ans