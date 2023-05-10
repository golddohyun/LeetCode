class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        tmp = matrix.copy()
        while len(tmp) > 0 :
            ans.extend(tmp[0])
            tmp.remove(tmp[0])
            tmp = list(map(list, zip(*tmp)))[::-1]
        return ans