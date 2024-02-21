class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def build_graph(edges):
            n = len(edges)
            graph = {}
            for i in range(1,n+1):
                graph[i] = []

            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            return graph
        
        graph = build_graph(edges)
        degree = {key: len(graph[key]) for key in graph.keys()}
        queue = [node for node in degree.keys() if degree[node] == 1 ]

        while queue:
            node = queue.pop(0)
            neigh = graph[node][0]
            graph.pop(node)
            graph[neigh].remove(node)

            degree.pop(node) # node degree is 0, remove it
            degree[neigh] -= 1

            if degree[neigh] == 1:
                queue.append(neigh)
        
        for u, v in edges[::-1]:
            if u in graph and v in graph:
                return [u,v]        
