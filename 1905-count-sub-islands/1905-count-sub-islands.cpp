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
    bool bfs(queue<pair<int, int>>& Q, vector<vector<int>>& visited, vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        bool is_sub = true;
        while (!Q.empty()){
            pair<int, int> cur = Q.front(); Q.pop();
            for (int dir=0; dir < 4; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if (nx < 0 || ny < 0 || nx >= grid2.size() || ny >= grid2[0].size()) continue;
                if (grid2[nx][ny] == 1 && visited[nx][ny] == 0) {
                    Q.push({nx, ny});
                    visited[nx][ny] =1;
                    if (grid1[nx][ny] == 0) is_sub = false;
                }

            }
        }
        return is_sub;
    }

    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int row = grid2.size(); int col = grid2[0].size();
        vector<vector<int>> visited(row, vector<int>(col, 0));
        queue<pair<int, int>> Q;
        int cnt=0;

        for (int i=0; i < row;  i++){
            for (int j=0; j < col; j++){
                if (!visited[i][j] && grid2[i][j] == 1 && grid1[i][j] == 1) {
                    visited[i][j] = 1;
                    Q.push({i, j});
                    if (bfs(Q, visited, grid1, grid2)) {
                        cnt++;
                    }
                }
            }
        }
        return cnt; 
    }
};