class Solution(object):
    def nearestExit(self, maze, entrance):
        from collections import deque
        row, col = len(maze), len(maze[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque([(entrance[0], entrance[1], 0)]) # x, y, distance
        maze[entrance[0]][entrance[1]] = "F" # Marked as visited
        min_dist = float('inf')
        
        while queue:
            curx, cury, dist = queue.popleft()
            if (curx in [0, row-1] or cury in [0, col-1]) and [curx, cury] != entrance:
                min_dist = min(min_dist, dist)
            for dr, dc in directions:
                nx, ny = curx + dr, cury + dc
                if 0 <= nx < row and 0 <= ny < col and maze[nx][ny] == ".":
                    queue.append((nx, ny, dist + 1))
                    maze[nx][ny] = "F"
        
        return min_dist if min_dist != float('inf') else -1