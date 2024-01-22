class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if len(grid) == 0 : return -1
        
        queue, maxval = deque(), 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]


        ## initialize : put grids that's rotten
        zero_flag = False
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 2 :
                    queue.append([r, c])
                    zero_flag = True
                elif grid[r][c] == 1 :
                    zero_flag = True
        
        while queue :
            curx, cury = queue.popleft()
            for dr, dc in directions :
                nx, ny = curx + dr, cury + dc
                if (nx < 0 or ny < 0 or nx >= rows or ny >= cols) : continue
                if grid[nx][ny] != 1 : continue # already rotten or is empty
                queue.append([nx, ny])
                grid[nx][ny] += grid[curx][cury]
            if maxval < grid[curx][cury] :
                maxval = grid[curx][cury]

        # filtering
        if not zero_flag : return 0
        if maxval == 0 : return -1
        for items in grid :
            if 1 in items :
                return -1
        return maxval-2


