class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.max_length(answerKey, k, 'T'), self.max_length(answerKey, k, 'F'))

    def max_length(self, answerKey, k, target):
        left = 0
        max_len = 0
        for right in range(len(answerKey)):
            if answerKey[right] != target:
                k -= 1
            if k < 0:
                if answerKey[left] != target:
                    k += 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len



# Time Exceeded Error : O(N^2) method
class Solution:
    def find_helper(sp_t, k, spl_by) : 
        ml = 0
        for s in range(k+1):
            result = []
            for i in range(len(sp_t)-s):
                temp_str = spl_by.join(sp_t[i:i+s+1])
                result.append(temp_str)
            ml = max(ml, max([len(i) for i in result], default=0))
        return ml
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ml_f = find_helper(a.split('F'), k, 'T')
        ml_t = find_helper(a.split('T'), k, 'F')
        return max(ml_f, ml_t)
