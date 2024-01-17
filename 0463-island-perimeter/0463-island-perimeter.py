class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        from collections import deque
        queue, cnt = deque(), 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        

        # 단일 열 또는 단일 행인 경우
        if rows == 1 or cols == 1:
            perimeter = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        # 단일 행 또는 열에서 각 셀은 둘레에 4면을 기여함
                        perimeter += 4
                        # 인접한 셀이 있으면 그 셀과의 공유 면을 뺌
                        if r > 0 and grid[r-1][c] == 1:
                            perimeter -= 2
                        if c > 0 and grid[r][c-1] == 1:
                            perimeter -= 2
            return perimeter

        # get the starting point (initial point)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append([r, c])
                    visited[r][c] = 1
                    break
            if queue:
                        break

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # visited true for initial point
        numzero, ans = 0, 0
        while queue:
            curx, cury = queue.popleft()
            visited[curx][cury] = 1
            numzero = 0
            for dr, dc in directions:
                nx, ny = curx + dr, cury + dc
                if (nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0])):
                    continue
                if grid[nx][ny] == 0 :
                    numzero +=1
            # 가장자리는 2개씩 더 세주기
            if ((curx ==0 and cury ==0) or (curx == 0 and cury == cols-1) 
                or (curx ==rows-1 and cury == 0) or (curx ==rows-1 and cury==cols-1)) :
                  numzero +=2
            elif curx == 0 or cury == 0 or curx == rows-1 or cury == cols -1 :
                  numzero+=1
            ans +=numzero
            for dr, dc in directions:
                nx, ny = curx + dr, cury + dc
                if (nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0])):
                    continue
                if (grid[nx][ny] == 1 and visited[nx][ny]==0):
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

        return ans