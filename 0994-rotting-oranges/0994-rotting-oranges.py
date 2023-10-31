from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        if N == 0 : 
            return -1

        visited = [[0]*M for _ in range(N)]
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Initialize the queue with rotten oranges
        queue = deque()
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 2:
                    queue.append((y, x))
                    visited[y][x] = 1
                    grid[y][x] = 0

        while queue:
            y, x = queue.popleft()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and grid[ny][nx] != 0:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    grid[ny][nx] = 0

        # Check for any remaining fresh oranges
        for row in grid:
            if 1 in row:
                return -1
            
        if max(map(max, visited)) == 0:
            return 0
        

        # Return time taken (max distance - 1)
        return max(map(max, visited)) - 1
