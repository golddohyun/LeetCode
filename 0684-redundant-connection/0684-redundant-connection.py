class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        adj_list = {key :[] for key in range(1, len(edges)+1)}
        for u, v in edges :
            adj_list[u].append(v)
            adj_list[v].append(u)

        
        def bfs_cycle_exists(adj_list) :
            for V in range(1, len(edges)+1) :
                if not adj_list[V] : continue
                visited = [0]*(len(edges)+1)
                pred = dict()
                Q = deque([V])
                pred[V] = -1
                
                while Q :
                    cur = Q.popleft()
                    visited[cur] =1
                    
                    for nei in adj_list[cur] :
                        if not visited[nei] :
                            visited[nei] =1
                            Q.append(nei)
                            pred[nei] = cur
                        elif pred[cur] != nei :
                            return True
            return False
                            
        
        for u, v in reversed(edges) :
            adj_list[u].remove(v)
            adj_list[v].remove(u)
            if not bfs_cycle_exists(adj_list):
                return [u, v]
            adj_list[u].append(v)
            adj_list[v].append(u)
            
