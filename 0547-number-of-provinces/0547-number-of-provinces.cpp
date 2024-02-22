class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int row = isConnected.size();
        int col = isConnected[0].size();
        vector<int> visited(row, 0);
        int prov = 0;
        for (int area=0; area < row; area++) {
            if (visited[area]) continue;
            visited[area] = 1;
            queue<int> Q;
            Q.push(area);
            prov++;
            while (!Q.empty()) {
                int curarea = Q.front(); Q.pop();

                for (int idx=0; idx < row; idx++) {
                    if (curarea != idx && visited[idx] !=1 && isConnected[curarea][idx]==1) {
                        visited[idx] =1;
                        Q.push(idx);
                    }
                }
            }
        }
        return prov;
    }
};