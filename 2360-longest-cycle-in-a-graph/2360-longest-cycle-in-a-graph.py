from collections import deque

class Solution(object):
    def longestCycle(self, edges):
        max_cycle_length = -1 
        visited = [-1] * len(edges) 

        for V in range(len(edges)):
            if edges[V] < 0 or visited[V] != -1: continue
            q = deque([(V, 0)])  
            index_in_path = {}  

            while q:
                cur, dist = q.popleft()
                if visited[cur] != -1: continue
                visited[cur] = dist
                index_in_path[cur] = dist 
                nei = edges[cur]
                
                if nei >= 0:
                    if visited[nei] == -1:  # If neighbor not visited
                        q.append((nei, dist + 1))
                    elif nei in index_in_path:  # Cycle detected
                        cycle_length = dist - index_in_path[nei] + 1
                        max_cycle_length = max(max_cycle_length, cycle_length)
                        break  

        return max_cycle_length