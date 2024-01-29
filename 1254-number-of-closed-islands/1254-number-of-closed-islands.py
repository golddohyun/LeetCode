class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        def bfs(queue) :
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue :
                curx, cury = queue.popleft()
                for dr, dc in directions :
                    nx, ny = curx+dr, cury+dc
                    if (nx < 0 or ny < 0  or nx >= len(grid) or ny >= len(grid[0])) : continue
                    if (grid[nx][ny] != 0 ) : continue
                    queue.append([nx, ny])
                    grid[nx][ny] = -2
        
        # initialize 
        rows, cols = len(grid), len(grid[0])
        queue, cnt = deque(), 0

        ## first visit the grid at the first and the last axis & value of grid == 0 
        for r in range(rows) :
            for c in range(cols) :
                if (r in [0, rows-1] or c in [0, cols-1]) and grid[r][c] == 0 :
                    queue.append([r, c])
                    grid[r][c] = -2 # marked as visited
                    bfs(queue)

        ## run bfs within valid choices
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 0 :
                    queue.append([r, c])
                    grid[r][c] = -2
                    bfs(queue)
                    cnt +=1
        return cnt
        