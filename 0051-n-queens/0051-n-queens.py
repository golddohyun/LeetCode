class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        isused1 = [0]*n
        isused2, isused3 = [0]*(2*n-1), [0]*(2*n-1)
        q_arr = [["." for _ in range(n)] for _ in range(n)]
        import copy

        def nqueen(numrow, q_arr, result):
            if numrow == n:
                result.append(["".join(row) for row in copy.deepcopy(q_arr)])
                return
            for idx in range(n):
                if isused1[idx] or isused2[idx+numrow] or isused3[numrow-idx+n-1]:
                    continue
                isused1[idx] = 1
                isused2[idx+numrow] = 1
                isused3[numrow-idx+n-1] = 1
                q_arr[numrow][idx] = "Q"
                nqueen(numrow+1, q_arr, result)
                isused1[idx] = 0
                isused2[idx+numrow] = 0
                isused3[numrow-idx+n-1] = 0
                q_arr[numrow][idx] = "."

        result = []
        nqueen(0, q_arr, result)
        return result