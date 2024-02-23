class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        for V in range(len(graph)) :
            color = [-1]*len(graph)
            visited = [0]*len(graph)
            Q = deque([V])
            color[V] = 1
            while Q :
                cur = Q.popleft()
                visited[cur] = 1
                for nei in graph[cur] : 
                    if (not visited[nei] and color[cur] == 1 and color[nei] ==-1) : 
                        Q.append(nei)
                        color[nei] = 0
                        visited[nei] =1
                    elif (not visited[nei] and  color[cur]==0  and color[nei]== -1) :
                        Q.append(nei)
                        color[nei] =1
                        visited[nei] =1
                    elif (color[cur]!= -1 and color[nei] == color[cur]) :
                        return False
        return True