class Solution(object):
    def create_alphabet_dictionary(self):
        alphabet_dict = {}
        current_char_code = ord('a')  
        for i in range(2, 10):
            char_count = 4 if i in [7, 9] else 3
            alphabet_dict[str(i)] = [chr(current_char_code + j) for j in range(char_count)]
            current_char_code += char_count
        return alphabet_dict

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits : return []
        alpha_dct = self.create_alphabet_dictionary()
        result, used = [], [[0]*len(alpha_dct[i]) for i in digits]
        def backtrack_perm(depth, arr, result) :
            if len(arr) == len(digits) :
                result.append(''.join(arr[:]))
                return
            for i in range(len(alpha_dct[digits[depth]])) :
                if not used[depth][i] :
                    used[depth][i] == True
                    arr.append(alpha_dct[digits[depth]][i])
                    backtrack_perm(depth+1, arr, result)
                    arr.pop()
                    used[depth][i] == False

        backtrack_perm(0, [], result)
        return result
