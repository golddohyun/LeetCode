class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """        
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        row, col = len(grid2), len(grid2[0])
        visited = [[0] * col for _ in range(row)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            is_sub_island = True
            
            while queue:
                cur_r, cur_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid2[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
                        if grid1[nr][nc] == 0:
                            is_sub_island = False
            return is_sub_island

        cnt = 0
        for r in range(row):
            for c in range(col):
                if not visited[r][c] and grid2[r][c] == 1 and grid1[r][c] == 1:
                    visited[r][c] = 1
                    if bfs(r, c):
                        cnt += 1
                        
        return cnt
