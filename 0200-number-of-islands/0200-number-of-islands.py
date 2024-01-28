from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*col for _ in range(row)]
        queue, cnt = deque(), 0
        for i in range(row) :
            for j in range(col) :
                if visited[i][j] == 1 or grid[i][j] == "0" : continue
                queue.append([i,j])
                visited[i][j] = 1
                while queue :
                    curx, cury = queue.popleft()
                    for dr, dc in directions :
                        nx, ny = curx + dr, cury + dc
                        if (nx < 0 or ny < 0 or nx >= row or ny >=col) : continue
                        if (visited[nx][ny] == 1 or grid[nx][ny] == "0") : continue
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                cnt +=1
        return cnt