class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack_comb(start, arr, result) :
            if len(arr) == k :
                result.append(arr[:])
            for i in range(start, n+1) :
                arr.append(i)
                backtrack_comb(i+1, arr, result)
                arr.pop()
        
        result=[]
        backtrack_comb(1, [], result)
        return result