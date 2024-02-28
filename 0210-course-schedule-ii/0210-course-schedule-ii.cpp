class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans;
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        queue<int> Q;

        // get adjacent listand indegree list
        for (auto& i : prerequisites){
            int course  = i[0];
            int prelim = i[1];
            adj[prelim].push_back(course);
            indegree[course]++;
        }

       for (int i=0; i < numCourses; i++) {
          if (indegree[i] == 0) Q.push(i);
       }

       while (!Q.empty()){
          int cur = Q.front(); Q.pop();
          ans.push_back(cur);
          for (auto &nei : adj[cur]){
              if (--indegree[nei] == 0){
                  Q.push(nei);
              }
          }
       }
      
      if (ans.size() != numCourses) return {};
      return ans;
    }
};