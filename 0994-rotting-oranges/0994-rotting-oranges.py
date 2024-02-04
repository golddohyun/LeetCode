class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*col for _ in range(row)]
        maxdst, queue = -1, deque()

        for r in range(row) :
            for c in range(col) :
                if grid[r][c] == 2 :
                    queue.append([r, c, 0]) # x, y, distance
                    visited[r][c] = -1

        while queue :
            curx, cury, dist = queue.popleft()
            maxdst = max(maxdst, dist)
            for dr, dc in directions :
                nx, ny = curx+dr, cury+dc
                if (0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 0 and grid[nx][ny] == 1) :
                    queue.append([nx, ny, dist+1])
                    visited[nx][ny] = 1

        visit_1, grid_1 = sum(row.count(1) for row in visited),  sum(row.count(1) for row in grid)

        if visit_1 != grid_1 : return -1
        if visit_1 == 0 : return 0

        return maxdst