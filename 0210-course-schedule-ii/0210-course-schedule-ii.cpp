class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> deg(numCourses, 0);
        vector<int> result;
        // get adjacent list and indegree list
        for(auto& i : prerequisites){
            adj[i[1]].push_back(i[0]);
            deg[i[0]]++;
        }
        queue<int> Q;
        for (int i =0; i < numCourses; i++){
            if(deg[i] == 0) Q.push(i);
        }
        
        for(int i = 0; i < numCourses; i++){

            //cycle exists
            if (Q.empty()){
                return {};
            }
            int x = Q.front();
            Q.pop();
            result.push_back(x);
            for (int i=0; i < adj[x].size(); i++){
                int y = adj[x][i];
                if (--deg[y] == 0) Q.push(y);
            }
        }
        return result;
    }
};