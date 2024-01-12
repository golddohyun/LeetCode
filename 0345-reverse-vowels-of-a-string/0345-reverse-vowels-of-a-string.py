class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        idxlst = [i for i in range(len(s)) if s[i] in "aeiouAEIOU"]
        rev = [i for i in s if i in "aeiouAEIOU"][::-1]
        anslst = list(s)
        for i in range(len(idxlst)) :
            anslst[idxlst[i]] = rev[i]
        return ''.join(anslst)
        