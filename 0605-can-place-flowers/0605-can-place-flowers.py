class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        validnum=0
        for idx in range(len(flowerbed)) :
            if flowerbed[idx] == 0: 
                if (idx == 0 or flowerbed[idx-1] ==0) and (idx == len(flowerbed)-1 or flowerbed[idx+1] == 0) : 
                    flowerbed[idx] =1
                    validnum +=1
        if n > validnum :
            return False
        return True
