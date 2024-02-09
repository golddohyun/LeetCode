class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack_comb(start, arr, target) :
            if len(arr)==k and target == 0 :
                result.append(arr[:])
                print(result)
                return
            for num in range(start, 10):
                backtrack_comb(num+1, arr+[num], target-num)

        result = []
        backtrack_comb(1, [], n)
        return result