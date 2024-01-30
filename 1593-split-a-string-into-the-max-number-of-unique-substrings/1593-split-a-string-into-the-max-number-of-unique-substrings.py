class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = set()
        uniq_subst = set()
        def backtrack_perm(s, start, uniq_subst, result):
            if start == len(s):
                result.add(tuple(uniq_subst.copy()))
                return

            for idx in range(start, len(s)) :
                if s[start:idx+1] not in uniq_subst :
                    uniq_subst.add(s[start:idx+1])
                    backtrack_perm(s, idx+1, uniq_subst, result)
                    uniq_subst.discard(s[start:idx+1])
                    
        backtrack_perm(s, 0, uniq_subst, result)
        max_val = 0
        for item in result :
            if len(item) > max_val :
                max_val = len(item)
        return max_val