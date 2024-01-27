class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # import string
        # d = dict.fromkeys(string.ascii_lowercase, 0)
        d = {chr(i): 0 for i in range(97, 123)}
        for l in s1 : d[l] +=1

        start, end = 0, len(s1)-1
        while end < len(s2) :
            hash_copy = d.copy()
            for item in s2[start:end+1] :
                if hash_copy[item] > 0 :
                    hash_copy[item] -=1
            if sum(hash_copy.values()) == 0 :
                return True
            else : 
                start+=1
                end+=1
        return False