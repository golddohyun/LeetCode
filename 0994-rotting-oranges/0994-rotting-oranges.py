class Solution(object):
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        fresh_oranges = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # x, y, distance
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        max_dist = 0
        while queue:
            curx, cury, dist = queue.popleft()
            max_dist = max(max_dist, dist)
            for dr, dc in directions:
                nx, ny = curx + dr, cury + dc
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                    grid[nx][ny] = 2 # Mark as rotten
                    fresh_oranges -= 1
                    queue.append((nx, ny, dist + 1))

        if fresh_oranges > 0:
            return -1
        return max_dist