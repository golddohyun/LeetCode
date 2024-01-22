class Solution(object):
    def permute(self, data, i, length, result):
        if i == length:
            result.append(''.join(data))
        else:
            # Proceed without changing the current character
            self.permute(data, i + 1, length, result)
            if data[i].isalpha():
                data[i] = data[i].swapcase() 
                self.permute(data, i + 1, length, result)
                data[i] = data[i].swapcase()  # Revert the case change

    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.permute(list(s), 0, len(s), ans)
        return ans
