class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected)
        adjacency_list = {key : [] for key in range(len(isConnected))} #0,1,2

        for i in range(len(isConnected)) :
            for j in range(len(isConnected[0])) :
                if i !=j and isConnected[i][j] ==1 :
                    adjacency_list[i].append(j)

        prov = 0
        for area in range(len(isConnected)) :
            if visited[area] : continue
            visited[area] = 1
            q = deque([area])
            prov+=1
            while q :
                curarea = q.popleft()
                for nei in adjacency_list[curarea] :
                    if visited[nei] : continue
                    visited[nei] = 1
                    q.append(nei)
        return prov