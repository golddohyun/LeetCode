class Solution:
    def dfs(self, visited, graph, i):
        if visited[i] == 2:
            return True
        if visited[i] == 1:
            return False
        visited[i] = 1
        for v in graph[i]:
            if not self.dfs(visited, graph, v):
                return False
        visited[i] = 2
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites : 
            adj[pre[1]].append(pre[0])

        visited = [False for _ in range(len(adj))]

        for i in range(numCourses):
            self.dfs(visited, adj, i)
        if set(visited) == {2} :
            return True
        else :
            return False