class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        from collections import defaultdict, deque
        adjacency_list = defaultdict(list)
        visited = [0]*n
        for u, v in edges :
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        q = deque([source])
        while q :
            cur = q.popleft()
            visited[cur] = 1
            if (cur == destination) : return True
            for nei in adjacency_list[cur] :
                if visited[nei] : continue
                visited[nei] = 1
                q.append(nei)
        return False

