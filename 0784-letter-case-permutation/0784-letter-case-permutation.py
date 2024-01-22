class Solution(object):
    def swapcase(self, data, idx) :
        if data[idx].islower() :
            data[idx] = data[idx].upper()
        else :
            data[idx] = data[idx].lower()
    def permute(self, data, i, length, result):
        if i == length :
            result.append(''.join(data))
        else :
            # Include the current character as is
            self.permute(data, i + 1, length, result)

            if data[i].isalpha() :
                self.swapcase(data, i)
                self.permute(data, i+1, length, result)
                self.swapcase(data, i)
                
        return list(set(result))          
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 1 :
            if s[0].isalpha() :
                return [s.upper(), s.lower()]
        ans = self.permute(list(s), 0, len(s), [])
        return ans
