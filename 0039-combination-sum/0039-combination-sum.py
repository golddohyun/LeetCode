class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack_comb(arr, i, target) :
            if target == 0 :
                result.append(arr[:])
                return
            for idx in range(i, len(candidates)) :
                if candidates[idx] <= target :
                    backtrack_comb(arr+[candidates[idx]], idx, target-candidates[idx])

        result = []
        backtrack_comb([], 0, target)
        return list(result)