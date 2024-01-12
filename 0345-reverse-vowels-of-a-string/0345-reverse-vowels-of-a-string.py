class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## runtime 36ms (faster than 78%), Too much memory usage
        # idxlst = [i for i in range(len(s)) if s[i] in "aeiouAEIOU"]
        # rev = [i for i in s if i in "aeiouAEIOU"][::-1]
        # anslst = list(s)
        # for i in range(len(idxlst)) :
            # anslst[idxlst[i]] = rev[i]
        # return ''.join(anslst)

        left, right, slist = 0, len(s)-1, list(s)
        vowels=set('AEIOUaeiou')
        while left < right :
            if left < right and s[left] not in vowels :
                left +=1
            elif left < right and s[right] not in vowels :
                right -=1
            else :
                slist[left], slist[right] = slist[right], slist[left]
                left+=1
                right -=1
        return ''.join(slist)