class Solution {
public:
    vector<vector<long>> dp;
    int Mod = 1e9+7;
    vector<int> dj{0,1,0,-1};
    vector<int> di{-1,0,1,0};
    int getPaths(vector<vector<int>> &grid, int row, int col){
        if(dp[row][col]){
            return dp[row][col];
        }
        long long ans = 0;
        for(int d = 0; d < 4; d++){
            int i = row + di[d];
            int j = col + dj[d];
            if(i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size()){
                if(grid[i][j] > grid[row][col]){
                    ans = (ans + getPaths(grid, i, j))%Mod;
                }
            }
        }
        ans = (ans+1)%Mod;
        return dp[row][col] = ans;
    }
    int countPaths(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        dp.resize(m, vector<long>(n,0));
        long long ans = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(dp[i][j]){
                    ans = (ans+dp[i][j])%Mod;
                }else{
                    ans = (ans + getPaths(grid, i, j))%Mod;
                }
            }
        }
        return ans;
    }
};