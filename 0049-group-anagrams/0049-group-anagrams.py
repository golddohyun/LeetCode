class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for word in strs : 
            w_key = ''.join(sorted(word))
            if w_key not in str_dict :
                str_dict[w_key] = []
            str_dict[w_key].append(word)
        return sorted(str_dict.values(), key=lambda x : len(x))
