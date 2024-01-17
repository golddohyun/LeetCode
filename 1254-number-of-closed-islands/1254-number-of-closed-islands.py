## Memory Usage: 13.4 MB, less than 99.00%
## Runtime: 106 ms, faster than 39.00%
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])
        cnt = 0
        def dfs(x, y) :
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != 0:
                return 
            grid[x][y] = -2
            for dr, dc in directions : 
                nx, ny = x+dr , y+dc
                dfs(nx, ny)

        for r in range(rows) :
            for c in range(cols) :
                if (r in [0, rows-1] and grid[r][c] ==0) or (c in [0, cols-1] and grid[r][c] ==0) :
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols) :
                if grid[r][c] == 0 :
                    dfs(r,c)
                    cnt +=1
        return cnt