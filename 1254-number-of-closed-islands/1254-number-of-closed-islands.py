## Memory Usage: 13.4 MB, less than 99.00%
## Runtime: 106 ms, faster than 39.00%
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        def bfs(grid, queue):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue : # while queue is not empty
                curx, cury = queue.popleft()
                for dr, dc in directions :
                    nx, ny = curx +dr, cury+dc
                    if (nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0])): continue
                    if (grid[nx][ny] != 0) : continue
                    grid[nx][ny] = -2
                    queue.append([nx, ny])

        q, cnt = deque(), 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols) :
                if (r in [0, rows-1] and grid[r][c] ==0) or (c in [0, cols-1] and grid[r][c] ==0) :
                    q.append([r, c])
                    bfs(grid, q)

        for r in range(1, rows-1) :
            for c in range(1, cols-1) :
                if grid[r][c] == 0 : # if not visited and # of grid is 0
                    q.append([r, c])
                    bfs(grid, q)
                    # print(r, c)
                    cnt+=1
        return cnt