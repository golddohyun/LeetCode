from collections import deque 
class Solution:
    def dfs(self, graph, node, visited, path):
        visited[node] = True
        path[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                if self.dfs(graph, nei, visited, path):
                    return True
            elif path[nei]:
                return True

        path[node] = False  # no cycle found from this node, safe
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        path = [False] * n
        safe_nodes = []

        for node in range(n):
            if not self.dfs(graph, node, visited, path):
                safe_nodes.append(node)

        return safe_nodes
