#include <iostream>
#include <vector>
#include <queue>
#define X first
#define Y second
using namespace std;

class Solution {
public:
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    void bfs(queue<pair<int,int>>& Q, vector<vector<int>>& visited, vector<vector<int>>& grid) {
        while (!Q.empty()) {
            pair<int, int> cur = Q.front(); Q.pop();
            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if (nx < 0 || ny < 0 || nx >= grid.size() || ny >= grid[0].size()) continue;
                if (grid[nx][ny] == 1 || visited[nx][ny] == 1) continue;
                visited[nx][ny] = 1;
                Q.push({nx, ny});        
            }
        }
    }

    int closedIsland(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        vector<vector<int>> visited(row, vector<int>(col, 0));
        queue<pair<int,int>> Q;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (((i == 0 || i == row-1) || (j == 0 || j == col-1)) && grid[i][j] == 0 && visited[i][j] == 0) {
                    Q.push({i, j});
                    visited[i][j] = 1;
                    bfs(Q, visited, grid);
                }
            }
        }
        
        int cnt = 0;
        // Count and mark the closed islands
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (visited[i][j] == 0 && grid[i][j] == 0) {
                    Q.push({i, j});
                    visited[i][j] = 1;
                    bfs(Q, visited, grid);
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
};

// int main() {
//     vector<vector<int>> grid = {
//         {1,1,1,1,1,1,1,0},
//         {1,0,0,0,0,1,1,0},
//         {1,0,1,0,1,1,1,0},
//         {1,0,0,0,0,1,0,1},
//         {1,1,1,1,1,1,1,0}
//     };

//     Solution sol;
//     int result = sol.closedIsland(grid);
//     cout << "Number of closed islands: " << result << endl;

//     return 0;
// }
