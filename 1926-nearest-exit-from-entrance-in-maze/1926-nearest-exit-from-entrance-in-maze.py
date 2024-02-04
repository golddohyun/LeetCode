class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        from collections import deque
        row, col = len(maze), len(maze[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = 0
        min_cnt= float('inf')
        while queue :
            curx, cury = queue.popleft()
            if (curx in [0, row-1] or cury in [0, col-1]) and [curx, cury] != entrance :
                min_cnt = min(min_cnt, maze[curx][cury])
            for dr, dc in directions :
                nx, ny = curx+dr, cury+dc
                if (nx < 0 or ny < 0 or nx >=row or ny >=col) : continue
                if maze[nx][ny] != "." : continue
                queue.append([nx,ny])
                maze[nx][ny] = maze[curx][cury]+1


        if min_cnt == float('inf') :
            return -1

        return min_cnt