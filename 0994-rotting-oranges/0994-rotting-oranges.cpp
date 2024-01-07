class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size(); //numrows
        int m = grid[0].size(); //numcols
        vector<vector<int>> tracktime(n, vector<int>(m, 0));
        int dx[4] = {1, 0, -1, 0};
        int dy[4] = {0, 1, 0, -1};
        queue <pair<int, int>> Q;

        // if visited, i would mark the elements
        for (int i=0; i < n; i++){
            for (int j=0; j<m; j++){
                if (grid[i][j] == 2) {
                    Q.push({i,j});
                    tracktime[i][j] = 1;}
            }
        }

        while (!Q.empty()){
            pair<int, int> cur = Q.front();
            Q.pop();
            for (int dir=0; dir < 4; dir++){
                int nx = cur.first + dx[dir];
                int ny = cur.second + dy[dir];
                if (nx < 0 || nx >= n | ny < 0 || ny >=m ) continue;
                if (grid[nx][ny] != 1) continue;
                tracktime[nx][ny] = tracktime[cur.first][cur.second] + 1;
                grid[nx][ny] = 2;
                Q.push({nx, ny});
            }
        }
        // get max time
        int ans=0;
        for (int i=0; i < n; i++){
            for (int j=0; j<m; j++){
                if (ans < tracktime[i][j]) ans = tracktime[i][j];
                if (grid[i][j] == 1) return -1;
            }
        }
        if (ans==0) return 0;
        return ans -1;

    }
};
