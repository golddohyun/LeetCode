class Solution:
    def __init__(self):
        self.dp = []
        self.Mod = int(1e9) + 7
        self.dj = [0, 1, 0, -1]
        self.di = [-1, 0, 1, 0]
    
    def getPaths(self, grid, row, col):
        if self.dp[row][col]:
            return self.dp[row][col]
        
        ans = 0
        for d in range(4):
            i = row + self.di[d]
            j = col + self.dj[d]
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] > grid[row][col]:
                    ans = (ans + self.getPaths(grid, i, j)) % self.Mod
        
        ans = (ans + 1) % self.Mod
        self.dp[row][col] = ans
        return ans
    
    def countPaths(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.dp = [[0] * n for _ in range(m)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if self.dp[i][j]:
                    ans = (ans + self.dp[i][j]) % self.Mod
                else:
                    ans = (ans + self.getPaths(grid, i, j)) % self.Mod
        
        return ans