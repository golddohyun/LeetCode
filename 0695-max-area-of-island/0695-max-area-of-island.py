class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        queue , max_cnt = deque(), 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for r in range(rows) :
            for c in range(cols) :
                if visited[r][c] == 0 and grid[r][c] == 1 :
                    cnt = 0
                    queue.append([r,c])
                    visited[r][c] = 1
                    while queue :
                        curx, cury = queue.popleft()
                        cnt +=1
                        for dr, dc in directions :
                            nx, ny = curx+dr, cury+dc
                            if (nx < 0 or ny < 0  or nx >= rows or ny >= cols) : continue
                            if (visited[nx][ny] == 1 or grid[nx][ny] == 0) : continue
                            queue.append([nx,ny])
                            visited[nx][ny] = 1
                    if max_cnt < cnt : max_cnt = cnt
        return max_cnt