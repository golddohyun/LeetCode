class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        paths= {key :[] for key in range(1, n+1)}
        for u, v in edges :
            paths[u].append(v)
            paths[v].append(u)

        ## implement cycle detection without indegree approach
        def bfs_cycle_exists(paths, n) :
            for V in range(1, n+1) :
                visited = [0]*(n+1)
                parent = [-1]*(n+1)
                q = deque([V])
                while q :
                    cur = q.popleft()
                    visited[cur]=1
                    for nei in paths[cur] :
                        if not visited[nei] :
                            q.append(nei)
                            parent[nei] = cur
                        elif parent[cur] != nei :
                            return True
            return False

        for u, v in reversed(edges) :
            paths[u].remove(v)
            paths[v].remove(u)
            if not bfs_cycle_exists(paths, n) :
                return [u, v]
            paths[u].append(v)
            paths[v].append(u)