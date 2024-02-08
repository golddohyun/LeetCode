class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
  
        def backtrack_comb(arr, result, target) :
            if target == 0 and sorted(arr[:]) not in result :
                result.append(sorted(arr[:]))
                return
            for i in range(len(candidates)) :
                if candidates[i] <= target :
                    arr.append(candidates[i])
                    backtrack_comb(arr, result, target-candidates[i])
                    arr.pop()

        result = []
        backtrack_comb([], result, target)
        return list(result)