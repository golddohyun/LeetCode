class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        # Using a set to store cycles for O(1) look-up
        cycles = set()
        visited = [-1] * len(edges) # -1 indicates unvisited

        for V in range(len(edges)):
            if edges[V] < 0: continue

            if visited[V] != -1: continue # Skip if already visited

            q = [V]
            index_in_path = {V: 0} # Store index in the path for each node
            while q:
                cur = q.pop()
                if edges[cur] < 0: continue

                nei = edges[cur]
                if visited[nei] == -1: # If neighbor not visited
                    visited[nei] = visited[cur] + 1
                    q.append(nei)
                    index_in_path[nei] = visited[nei]
                elif nei in index_in_path: # Found a cycle
                    # No need to sort, just get the cycle length directly
                    cycle_length = visited[cur] - index_in_path[nei] + 1
                    cycles.add(tuple(range(index_in_path[nei], visited[cur] + 1)))
                    break

            # Mark all nodes in the path as visited
            for node in index_in_path.keys():
                visited[node] = 0 # Reset to 0 to indicate node is no longer in the current path

        if not cycles:
            return -1
        return max(len(i) for i in cycles)