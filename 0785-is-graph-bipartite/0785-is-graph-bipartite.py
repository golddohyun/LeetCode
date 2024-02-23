class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        color = [-1] * len(graph) 

        for V in range(len(graph)):
            if color[V] == -1:  
                Q = deque([V])
                color[V] = 1  
                while Q:
                    cur = Q.popleft()
                    for nei in graph[cur]:
                        if color[nei] == -1: 
                            Q.append(nei)
                            color[nei] = 1 - color[cur]  
                        elif color[nei] == color[cur]: 
                            return False
        return True