class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
#         s = min(len(word1), len(word2))
#         newstr=''

#         for i in range(s) :
#             newstr+= word1[i]
#             newstr+= word2[i]
#         if len(word1) < len(word2) :
#             newstr +=word2[s:]
#         elif len(word2) < len(word1) :
#             newstr += word1[s:]
        s, newstr = min(len(word1), len(word2)), ''
        newstr = ''.join(word1[i] + word2[i] for i in range(s))
        newstr += word1[s:] + word2[s:]

        return newstr