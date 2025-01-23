from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0] * col for _ in range(row)]

        def bfs(x, y):
            queue = deque()
            visited[x][y] = 1
            queue.append((x, y))
            while queue:
                cur_x, cur_y = queue.popleft()
                for dr, dc in directions:
                    nx, ny = cur_x + dr, cur_y + dc
                    # Ver 1.
                    # if  (nx < 0 or ny < 0 or nx >= row or ny >=col) : continue
                    # if (visited[nx][ny] == 1 or grid[nx][ny] == "0") : continue
                    if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] != 1 and grid[nx][ny] == "1":
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

        n_islands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and visited[i][j] != 1:
                    bfs(i, j)
                    n_islands += 1

        return n_islands