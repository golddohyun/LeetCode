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
