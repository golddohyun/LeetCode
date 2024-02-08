class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack_comb(start, arr, target) :
            if target == 0 :
                result.append(arr[:])
                return
            prev = -1
            for i in range(start, len(candidates)) :
                if i > start and candidates[i] == prev :
                    continue
                if candidates[i] > target: break
                prev = candidates[i]
                backtrack_comb(i+1, arr+[candidates[i]], target-candidates[i])

        result = []
        candidates.sort()
        backtrack_comb(0, [], target)
        return result
  