class Solution(object):
    def kthPalindrome(self, queries, intLength):
        result=[]
        if intLength%2==0:
            base = 10**((intLength)//2 -1 )
            maxi = 9 * (10**(intLength//2 -1))
        else:
            base = 10**((intLength)//2)
            maxi = 9 * (10**(intLength//2))

        for i in queries :
            if i > maxi : 
                result.append(-1)
                continue
            temp = base + i-1
            if intLength%2==0:
                temp1 = str(temp) + str(temp)[-1::-1]
            else:
                temp1 = str(temp) + str(temp)[-2::-1]
            result.append(int(temp1))
        return result