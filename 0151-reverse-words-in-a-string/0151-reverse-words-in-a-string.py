class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return ' '.join(s.strip().split()[::-1])

        ans = []
        tmp = ""
        for let in s:
            if let != " ":
                tmp += let
            elif tmp:
                ans.append(tmp)
                tmp = ""
        # Add the last word if it exists
        if tmp:
            ans.append(tmp)
        return ' '.join(ans[::-1])
        