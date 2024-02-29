class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(mystr):
            start, end = 0, len(mystr)-1
            while start < end :
                if mystr[start] != mystr[end] :
                    return False
                start+=1
                end-=1
            return True


        def backtrack_pal(s, start, path, result):
            if start == len(s):  
                result.append(path[:])
                return
            
            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1]) 
                    backtrack_pal(s, end+1, path, result)  
                    path.pop() 

        result = []
        backtrack_pal(s, 0, [], result)
        return result