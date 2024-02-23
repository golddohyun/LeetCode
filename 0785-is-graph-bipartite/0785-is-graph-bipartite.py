class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        for V in range(len(graph)) :
            red = [0]*len(graph)
            blue = [0]*len(graph)
            visited = [0]*len(graph)

            # starting point = V
            Q = deque([V])
            red[V] = 1

            while Q :
                cur = Q.popleft()
                visited[cur] =1
                for nei in graph[cur] : 
                    if (not visited[nei] and red[cur] ==1 and blue[nei] == 0) : 
                        Q.append(nei)
                        blue[nei] = 1
                        visited[nei] =1
                    elif (not visited[nei] and  blue[cur]==1 and red[nei]== 0) :
                        Q.append(nei)
                        red[nei] =1
                        visited[nei] =1
                    elif (red[nei] == red[cur] or blue[nei] == blue[cur]) :
                        return False

        return True